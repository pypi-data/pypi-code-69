# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.17
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayerGameAthletes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'stat': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stat': 'stat'
    }

    def __init__(self, id=None, name=None, stat=None):  # noqa: E501
        """PlayerGameAthletes - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._stat = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if stat is not None:
            self.stat = stat

    @property
    def id(self):
        """Gets the id of this PlayerGameAthletes.  # noqa: E501


        :return: The id of this PlayerGameAthletes.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayerGameAthletes.


        :param id: The id of this PlayerGameAthletes.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PlayerGameAthletes.  # noqa: E501


        :return: The name of this PlayerGameAthletes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerGameAthletes.


        :param name: The name of this PlayerGameAthletes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def stat(self):
        """Gets the stat of this PlayerGameAthletes.  # noqa: E501


        :return: The stat of this PlayerGameAthletes.  # noqa: E501
        :rtype: str
        """
        return self._stat

    @stat.setter
    def stat(self, stat):
        """Sets the stat of this PlayerGameAthletes.


        :param stat: The stat of this PlayerGameAthletes.  # noqa: E501
        :type: str
        """

        self._stat = stat

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PlayerGameAthletes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerGameAthletes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
