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


class PlayerGamePPAAveragePPA(object):
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
        'all': 'float',
        '_pass': 'float',
        'rush': 'float'
    }

    attribute_map = {
        'all': 'all',
        '_pass': 'pass',
        'rush': 'rush'
    }

    def __init__(self, all=None, _pass=None, rush=None):  # noqa: E501
        """PlayerGamePPAAveragePPA - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self.__pass = None
        self._rush = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if _pass is not None:
            self._pass = _pass
        if rush is not None:
            self.rush = rush

    @property
    def all(self):
        """Gets the all of this PlayerGamePPAAveragePPA.  # noqa: E501


        :return: The all of this PlayerGamePPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this PlayerGamePPAAveragePPA.


        :param all: The all of this PlayerGamePPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._all = all

    @property
    def _pass(self):
        """Gets the _pass of this PlayerGamePPAAveragePPA.  # noqa: E501


        :return: The _pass of this PlayerGamePPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this PlayerGamePPAAveragePPA.


        :param _pass: The _pass of this PlayerGamePPAAveragePPA.  # noqa: E501
        :type: float
        """

        self.__pass = _pass

    @property
    def rush(self):
        """Gets the rush of this PlayerGamePPAAveragePPA.  # noqa: E501


        :return: The rush of this PlayerGamePPAAveragePPA.  # noqa: E501
        :rtype: float
        """
        return self._rush

    @rush.setter
    def rush(self, rush):
        """Sets the rush of this PlayerGamePPAAveragePPA.


        :param rush: The rush of this PlayerGamePPAAveragePPA.  # noqa: E501
        :type: float
        """

        self._rush = rush

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
        if issubclass(PlayerGamePPAAveragePPA, dict):
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
        if not isinstance(other, PlayerGamePPAAveragePPA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
