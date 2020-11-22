# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class CreateOwnedAliasOptions(object):
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
    """
    openapi_types = {
        'email_address': 'str',
        'inbox_id': 'str',
        'name': 'str',
        'proxied': 'bool'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'inbox_id': 'inboxId',
        'name': 'name',
        'proxied': 'proxied'
    }

    def __init__(self, email_address=None, inbox_id=None, name=None, proxied=None, local_vars_configuration=None):  # noqa: E501
        """CreateOwnedAliasOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_address = None
        self._inbox_id = None
        self._name = None
        self._proxied = None
        self.discriminator = None

        if email_address is not None:
            self.email_address = email_address
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if name is not None:
            self.name = name
        if proxied is not None:
            self.proxied = proxied

    @property
    def email_address(self):
        """Gets the email_address of this CreateOwnedAliasOptions.  # noqa: E501

        Email address to be hidden behind alias  # noqa: E501

        :return: The email_address of this CreateOwnedAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CreateOwnedAliasOptions.

        Email address to be hidden behind alias  # noqa: E501

        :param email_address: The email_address of this CreateOwnedAliasOptions.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def inbox_id(self):
        """Gets the inbox_id of this CreateOwnedAliasOptions.  # noqa: E501

        Optional inbox ID to attach to alias. Emails received by this inbox will be forwarded to the alias email address  # noqa: E501

        :return: The inbox_id of this CreateOwnedAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this CreateOwnedAliasOptions.

        Optional inbox ID to attach to alias. Emails received by this inbox will be forwarded to the alias email address  # noqa: E501

        :param inbox_id: The inbox_id of this CreateOwnedAliasOptions.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def name(self):
        """Gets the name of this CreateOwnedAliasOptions.  # noqa: E501

        Optional name for alias  # noqa: E501

        :return: The name of this CreateOwnedAliasOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOwnedAliasOptions.

        Optional name for alias  # noqa: E501

        :param name: The name of this CreateOwnedAliasOptions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def proxied(self):
        """Gets the proxied of this CreateOwnedAliasOptions.  # noqa: E501

        Optional proxied flag. When proxied is true alias will forward the incoming emails to the aliased email address via a proxy inbox. A new proxy is created for every new email thread. By replying to the proxy you can correspond with using your email alias without revealing your real email address.  # noqa: E501

        :return: The proxied of this CreateOwnedAliasOptions.  # noqa: E501
        :rtype: bool
        """
        return self._proxied

    @proxied.setter
    def proxied(self, proxied):
        """Sets the proxied of this CreateOwnedAliasOptions.

        Optional proxied flag. When proxied is true alias will forward the incoming emails to the aliased email address via a proxy inbox. A new proxy is created for every new email thread. By replying to the proxy you can correspond with using your email alias without revealing your real email address.  # noqa: E501

        :param proxied: The proxied of this CreateOwnedAliasOptions.  # noqa: E501
        :type: bool
        """

        self._proxied = proxied

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
        if not isinstance(other, CreateOwnedAliasOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOwnedAliasOptions):
            return True

        return self.to_dict() != other.to_dict()
