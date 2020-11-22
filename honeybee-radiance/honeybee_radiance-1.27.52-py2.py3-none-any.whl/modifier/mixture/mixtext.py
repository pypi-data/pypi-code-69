"""Radiance Mixtext Mixture.

http://radsite.lbl.gov/radiance/refer/ray.html#Mixtext
"""
from .mixturebase import Mixture


# TODO: Implement the class. It's currently only a generic Radiance Primitive
class Mixtext(Mixture):
    """Radiance Mixtext Material.

    Mixtext uses one modifier for the text foreground, and one for the background:

    .. code-block:: shell

        mod mixtext id
        4 foreground background fontfile textfile
        0
        9+
                Ox Oy Oz
                Rx Ry Rz
                Dx Dy Dz
                [spacing]

    or:

    .. code-block:: shell

        mod mixtext id
        4+N
                foreground background fontfile .
                This is a line with N words ...
        0
        9+
                Ox Oy Oz
                Rx Ry Rz
                Dx Dy Dz
                [spacing]

    Args:
        identifier: Text string for a unique Mixture ID. Must not contain spaces
            or special characters. This will be used to identify the object across
            a model and in the exported Radiance files.
        modifier: Modifier. It can be primitive, mixture, texture or pattern.
            (Default: None).
        values: An array 3 arrays for primitive data. Each of the 3 sub-arrays
            refer to a line number in the radiance primitve definitions and the
            values in each array correspond to values occurring within each line.
        is_opaque: A boolean to indicate whether this primitive is opaque.
        dependencies: A list of primitives that this primitive depends on. This
            argument is only useful for defining advanced primitives that are
            defined based on other primitives. (Default: []).

    Properties:
        * identifier
        * display_name
        * values
        * modifier
        * dependencies
        * is_modifier
        * is_material
        * is_opaque
    """
    __slots__ = ()

    pass
