# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2303
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AccessControlledResource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'application': 'str',
        'name': 'str',
        'description': 'str',
        'actions': 'list[AccessControlledAction]',
        'identifier_parts': 'list[IdentifierPartSchema]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'application': 'application',
        'name': 'name',
        'description': 'description',
        'actions': 'actions',
        'identifier_parts': 'identifierParts',
        'links': 'links'
    }

    required_map = {
        'application': 'optional',
        'name': 'optional',
        'description': 'required',
        'actions': 'required',
        'identifier_parts': 'optional',
        'links': 'optional'
    }

    def __init__(self, application=None, name=None, description=None, actions=None, identifier_parts=None, links=None):  # noqa: E501
        """
        AccessControlledResource - a model defined in OpenAPI

        :param application: 
        :type application: str
        :param name: 
        :type name: str
        :param description:  (required)
        :type description: str
        :param actions:  (required)
        :type actions: list[lusid.AccessControlledAction]
        :param identifier_parts: 
        :type identifier_parts: list[lusid.IdentifierPartSchema]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._application = None
        self._name = None
        self._description = None
        self._actions = None
        self._identifier_parts = None
        self._links = None
        self.discriminator = None

        self.application = application
        self.name = name
        self.description = description
        self.actions = actions
        self.identifier_parts = identifier_parts
        self.links = links

    @property
    def application(self):
        """Gets the application of this AccessControlledResource.  # noqa: E501


        :return: The application of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this AccessControlledResource.


        :param application: The application of this AccessControlledResource.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def name(self):
        """Gets the name of this AccessControlledResource.  # noqa: E501


        :return: The name of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessControlledResource.


        :param name: The name of this AccessControlledResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AccessControlledResource.  # noqa: E501


        :return: The description of this AccessControlledResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessControlledResource.


        :param description: The description of this AccessControlledResource.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def actions(self):
        """Gets the actions of this AccessControlledResource.  # noqa: E501


        :return: The actions of this AccessControlledResource.  # noqa: E501
        :rtype: list[AccessControlledAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AccessControlledResource.


        :param actions: The actions of this AccessControlledResource.  # noqa: E501
        :type: list[AccessControlledAction]
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def identifier_parts(self):
        """Gets the identifier_parts of this AccessControlledResource.  # noqa: E501


        :return: The identifier_parts of this AccessControlledResource.  # noqa: E501
        :rtype: list[IdentifierPartSchema]
        """
        return self._identifier_parts

    @identifier_parts.setter
    def identifier_parts(self, identifier_parts):
        """Sets the identifier_parts of this AccessControlledResource.


        :param identifier_parts: The identifier_parts of this AccessControlledResource.  # noqa: E501
        :type: list[IdentifierPartSchema]
        """

        self._identifier_parts = identifier_parts

    @property
    def links(self):
        """Gets the links of this AccessControlledResource.  # noqa: E501


        :return: The links of this AccessControlledResource.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AccessControlledResource.


        :param links: The links of this AccessControlledResource.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccessControlledResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
