"""
A class to model hierarchies of objects following Directed Acyclic Graph structure.

The graph traversal queries use Postgresql's recursive CTEs to fetch an entire tree
of related node ids in a single query. These queries also topologically sort the ids
by generation.
"""

from django.apps import apps
from django.db import models, connection
from django.db.models import Case, When
from django.core.exceptions import ValidationError

from .exceptions import NodeNotReachableException
from .transformations import _ordered_filter
from .query_builders import (
    AncestorQuery,
    DescendantQuery,
    UpwardPathQuery,
    DownwardPathQuery,
    ConnectedGraphQuery
)


class NodeManager(models.Manager):
    def roots(self, node=None):
        """Returns a Queryset of all root Nodes, or optionally, the roots of a select node"""
        if node is not None:
            return node.roots()
        return self.filter(parents__isnull=True)

    def leaves(self, node=None):
        """Returns a Queryset of all leaf Nodes, or optionally, the leaves of a select node"""
        if node is not None:
            return node.leaves()
        return self.filter(children__isnull=True)


def node_factory(edge_model, children_null=True, base_model=models.Model):
    edge_model_table = edge_model._meta.db_table

    class Node(base_model):
        children = models.ManyToManyField(
            "self",
            blank=children_null,
            symmetrical=False,
            through=edge_model,
            related_name="parents",
        )

        objects = NodeManager()

        class Meta:
            abstract = True

        def get_foreign_key_field(self, fk_instance=None):
            """
            Provided a model instance, checks if the edge model has a ForeignKey field to the
            model class of that instance, and then returns the associated field name, else None.
            """
            if fk_instance is not None:
                for field in edge_model._meta.get_fields():
                    if field.related_model is fk_instance._meta.model:
                        # Return the first field that matches
                        return field.name
            return None

        def get_pk_name(self):
            """Sometimes we set a field other than 'pk' for the primary key.
            This method is used to get the correct primary key field name for the
            model so that raw queries return the correct information."""
            return self._meta.pk.name

        def ordered_queryset_from_pks(self, pks):
            """
            Generates a queryset, based on the current class and ordered by the provided pks
            """
            return _ordered_filter(self.__class__.objects, "pk", pks)

        def add_child(self, child, **kwargs):
            kwargs.update({"parent": self, "child": child})
            disable_check = kwargs.pop("disable_circular_check", False)
            cls = self.children.through(**kwargs)
            return cls.save(disable_circular_check=disable_check)

        def remove_child(self, child, delete_node=False):
            """Removes the edge connecting this node to child, and optionally deletes the child node as well"""
            if child in self.children.all():
                self.children.through.objects.get(parent=self, child=child).delete()
                if delete_node:
                    # Note: Per django docs:
                    # https://docs.djangoproject.com/en/dev/ref/models/instances/#deleting-objects
                    # This only deletes the object in the database; the Python instance will still
                    # exist and will still have data in its fields.
                    child.delete()

        def add_parent(self, parent, *args, **kwargs):
            return parent.add_child(self, **kwargs)

        def remove_parent(self, parent, delete_node=False):
            """Removes the edge connecting this node to parent, and optionally deletes the parent node as well"""
            if parent in self.parents.all():
                parent.children.through.objects.get(parent=parent, child=self).delete()
                if delete_node:
                    # Note: Per django docs:
                    # https://docs.djangoproject.com/en/dev/ref/models/instances/#deleting-objects
                    # This only deletes the object in the database; the Python instance will still
                    # exist and will still have data in its fields.
                    parent.delete()

        def ancestors_raw(self, **kwargs):
            return AncestorQuery(instance=self, **kwargs).raw_queryset()

        def ancestors(self, **kwargs):
            pks = [item.pk for item in self.ancestors_raw(**kwargs)]
            return self.ordered_queryset_from_pks(pks)

        def ancestors_count(self):
            return self.ancestors().count()

        def self_and_ancestors(self, **kwargs):
            pks = [self.pk] + [item.pk for item in self.ancestors_raw(**kwargs)][::-1]
            return self.ordered_queryset_from_pks(pks)

        def ancestors_and_self(self, **kwargs):
            pks = [item.pk for item in self.ancestors_raw(**kwargs)] + [self.pk]
            return self.ordered_queryset_from_pks(pks)

        def descendants_raw(self, **kwargs):
            return DescendantQuery(instance=self, **kwargs).raw_queryset()

        def descendants(self, **kwargs):
            pks = [item.pk for item in self.descendants_raw(**kwargs)]
            return self.ordered_queryset_from_pks(pks)

        def descendants_count(self):
            return self.descendants().count()

        def self_and_descendants(self, **kwargs):
            pks = [self.pk] + [item.pk for item in self.descendants_raw(**kwargs)]
            return self.ordered_queryset_from_pks(pks)

        def descendants_and_self(self, **kwargs):
            pks = [item.pk for item in self.descendants_raw(**kwargs)] + [self.pk]
            return self.ordered_queryset_from_pks(pks)

        def clan(self, **kwargs):
            """
            Returns a queryset with all ancestors, self, and all descendants
            """
            pks = (
                [item.pk for item in self.ancestors_raw(**kwargs)]
                + [self.pk]
                + [item.pk for item in self.descendants_raw(**kwargs)]
            )
            return self.ordered_queryset_from_pks(pks)

        def clan_count(self):
            return self.clan().count()

        def siblings(self):
            # Returns all nodes that share a parent with this node
            return self.siblings_with_self().exclude(pk=self.pk)

        def siblings_count(self):
            # Returns count of all nodes that share a parent with this node
            return self.siblings().count()

        def siblings_with_self(self):
            # Returns all nodes that share a parent with this node and self
            return self.__class__.objects.filter(
                parents__in=self.parents.all()
            ).distinct()

        def partners(self):
            # Returns all nodes that share a child with this node
            return self.partners_with_self().exclude(pk=self.pk)

        def partners_count(self):
            # Returns count of all nodes that share a child with this node
            return self.partners().count()

        def partners_with_self(self):
            # Returns all nodes that share a child with this node and self
            return self.__class__.objects.filter(
                children__in=self.children.all()
            ).distinct()

        def path_raw(self, ending_node, directional=True, **kwargs):
            """
            Returns shortest path from self to ending node, optionally in either
            direction. The resulting RawQueryset is sorted from root-side, toward
            leaf-side, regardless of the relative position of starting and ending nodes.
            """

            if self == ending_node:
                return [[self.pk]]

            path = DownwardPathQuery(
                starting_node=self, ending_node=ending_node, **kwargs
            ).raw_queryset()

            if len(list(path)) == 0 and not directional:
                path = UpwardPathQuery(
                    starting_node=self, ending_node=ending_node, **kwargs
                ).raw_queryset()

            if len(list(path)) == 0:
                raise NodeNotReachableException

            return path

        def path_exists(self, ending_node, **kwargs):
            try:
                return len(list(self.path_raw(ending_node, **kwargs))) >= 1
            except NodeNotReachableException:
                return False

        def path(self, ending_node, **kwargs):
            pks = [item.pk for item in self.path_raw(ending_node, **kwargs)]
            return self.ordered_queryset_from_pks(pks)

        def distance(self, ending_node, **kwargs):
            """
            Returns the shortest hops count to the target node
            """
            if self is ending_node:
                return 0
            else:
                return self.path(ending_node, **kwargs).count() - 1

        def is_root(self):
            """
            Check if has children and not ancestors
            """
            return bool(self.children.exists() and not self.parents.exists())

        def is_leaf(self):
            """
            Check if has ancestors and not children
            """
            return bool(self.parents.exists() and not self.children.exists())

        def is_island(self):
            """
            Check if has no ancestors nor children
            """
            return bool(not self.children.exists() and not self.parents.exists())

        def is_ancestor_of(self, ending_node, **kwargs):
            try:
                return len(self.path_raw(ending_node, **kwargs)) >= 1
            except NodeNotReachableException:
                return False

        def is_descendant_of(self, ending_node, **kwargs):
            return (
                not self.is_ancestor_of(ending_node, **kwargs)
                and len(self.path_raw(ending_node, directional=False, **kwargs)) >= 1
            )

        def is_sibling_of(self, ending_node):
            return ending_node in self.siblings()

        def is_partner_of(self, ending_node):
            return ending_node in self.partners()

        def node_depth(self):
            # Depth from furthest root
            # ToDo: Implement
            pass

        def connected_graph_raw(self, **kwargs):
            # Gets all nodes connected in any way to this node
            return ConnectedGraphQuery(instance=self, **kwargs).raw_queryset()

        def connected_graph(self, **kwargs):
            pks = [item.pk for item in self.connected_graph_raw(**kwargs)]
            return self.ordered_queryset_from_pks(pks)

        def descendants_tree(self):
            """
            Returns a tree-like structure with descendants
            # ToDo: Modify to use CTE
            """
            tree = {}
            for child in self.children.all():
                tree[child] = child.descendants_tree()
            return tree

        def ancestors_tree(self):
            """
            Returns a tree-like structure with ancestors
            # ToDo: Modify to use CTE
            """
            tree = {}
            for parent in self.parents.all():
                tree[parent] = parent.ancestors_tree()
            return tree

        def _roots(self, ancestors_tree):
            """
            Works on objects: no queries
            """
            if not ancestors_tree:
                return set([self])
            roots = set()
            for ancestor in ancestors_tree:
                roots.update(ancestor._roots(ancestors_tree[ancestor]))
            return roots

        def roots(self):
            """
            Returns roots nodes, if any
            # ToDo: Modify to use CTE
            """
            ancestors_tree = self.ancestors_tree()
            roots = set()
            for ancestor in ancestors_tree:
                roots.update(ancestor._roots(ancestors_tree[ancestor]))
            if len(roots) < 1:
                roots.add(self)
            return roots

        def _leaves(self, descendants_tree):
            """
            Works on objects: no queries
            """
            if not descendants_tree:
                return set([self])
            leaves = set()
            for descendant in descendants_tree:
                leaves.update(descendant._leaves(descendants_tree[descendant]))
            return leaves

        def leaves(self):
            """
            Returns leaves nodes, if any
            # ToDo: Modify to use CTE
            """
            descendants_tree = self.descendants_tree()
            leaves = set()
            for descendant in descendants_tree:
                leaves.update(descendant._leaves(descendants_tree[descendant]))
            if len(leaves) < 1:
                leaves.add(self)
            return leaves

        def descendants_edges(self):
            """
            Returns a queryset of descendants edges

            ToDo: Perform topological sort
            """
            return edge_model.objects.filter(
                parent__in=self.self_and_descendants(),
                child__in=self.self_and_descendants(),
            )

        def ancestors_edges(self):
            """
            Returns a queryset of ancestors edges

            ToDo: Perform topological sort
            """
            return edge_model.objects.filter(
                parent__in=self.self_and_ancestors(),
                child__in=self.self_and_ancestors(),
            )

        def clan_edges(self):
            """
            Returns a queryset of all edges associated with a given node
            """
            return self.ancestors_edges() | self.descendants_edges()

        @staticmethod
        def circular_checker(parent, child):
            if child in parent.self_and_ancestors():
                raise ValidationError("The object is an ancestor.")

    return Node



class EdgeManager(models.Manager):
    def from_nodes_queryset(self, nodes_queryset):
        """Provided a queryset of nodes, returns all edges where a parent and child
        node are within the queryset of nodes."""
        return _ordered_filter(self.model.objects, ["parent", "child"], nodes_queryset)

    def descendants(self, node, **kwargs):
        """
        Returns a queryset of all edges descended from the given node
        """
        return _ordered_filter(
            self.model.objects, "parent", node.self_and_descendants(**kwargs)
        )

    def ancestors(self, node, **kwargs):
        """
        Returns a queryset of all edges which are ancestors of the given node
        """
        return _ordered_filter(
            self.model.objects, "child", node.ancestors_and_self(**kwargs)
        )

    def clan(self, node, **kwargs):
        """
        Returns a queryset of all edges for ancestors, self, and descendants
        """
        return self.from_nodes_queryset(node.clan(**kwargs))

    def path(self, start_node, end_node, **kwargs):
        """
        Returns a queryset of all edges for the shortest path from start_node to end_node
        """
        return self.from_nodes_queryset(start_node.path(end_node, **kwargs))

    def validate_route(self, edges, **kwargs):
        """
        Given a list or set of edges, verify that they result in a contiguous route
        """
        # ToDo: Implement
        pass

    def sort(self, edges, **kwargs):
        """
        Given a list or set of edges, sort them from root-side to leaf-side
        """
        # ToDo: Implement
        pass


def edge_factory(
    node_model,
    concrete=True,
    base_model=models.Model,
):

    if isinstance(node_model, str):
        try:
            node_model_name = node_model.split(".")[1]
        except IndexError:

            node_model_name = node_model
    else:
        node_model_name = node_model._meta.model_name

    class Edge(base_model):
        parent = models.ForeignKey(
            node_model,
            related_name=f"{node_model_name}_child",
            on_delete=models.CASCADE,
        )
        child = models.ForeignKey(
            node_model,
            related_name=f"{node_model_name}_parent",
            on_delete=models.CASCADE,
        )

        objects = EdgeManager()

        class Meta:
            abstract = not concrete

        def save(self, *args, **kwargs):
            if not kwargs.pop("disable_circular_check", False):
                self.parent.__class__.circular_checker(self.parent, self.child)
            super().save(*args, **kwargs)

    return Edge
