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


class DownloadAttachmentDto(object):
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
        'base64_file_contents': 'str',
        'content_type': 'str',
        'size_bytes': 'int'
    }

    attribute_map = {
        'base64_file_contents': 'base64FileContents',
        'content_type': 'contentType',
        'size_bytes': 'sizeBytes'
    }

    def __init__(self, base64_file_contents=None, content_type=None, size_bytes=None, local_vars_configuration=None):  # noqa: E501
        """DownloadAttachmentDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base64_file_contents = None
        self._content_type = None
        self._size_bytes = None
        self.discriminator = None

        if base64_file_contents is not None:
            self.base64_file_contents = base64_file_contents
        if content_type is not None:
            self.content_type = content_type
        if size_bytes is not None:
            self.size_bytes = size_bytes

    @property
    def base64_file_contents(self):
        """Gets the base64_file_contents of this DownloadAttachmentDto.  # noqa: E501

        Base64 encoded string of attachment bytes. Decode the base64 string to get the raw file bytes  # noqa: E501

        :return: The base64_file_contents of this DownloadAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._base64_file_contents

    @base64_file_contents.setter
    def base64_file_contents(self, base64_file_contents):
        """Sets the base64_file_contents of this DownloadAttachmentDto.

        Base64 encoded string of attachment bytes. Decode the base64 string to get the raw file bytes  # noqa: E501

        :param base64_file_contents: The base64_file_contents of this DownloadAttachmentDto.  # noqa: E501
        :type: str
        """

        self._base64_file_contents = base64_file_contents

    @property
    def content_type(self):
        """Gets the content_type of this DownloadAttachmentDto.  # noqa: E501

        Content type of attachment  # noqa: E501

        :return: The content_type of this DownloadAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this DownloadAttachmentDto.

        Content type of attachment  # noqa: E501

        :param content_type: The content_type of this DownloadAttachmentDto.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def size_bytes(self):
        """Gets the size_bytes of this DownloadAttachmentDto.  # noqa: E501

        Size in bytes of attachment  # noqa: E501

        :return: The size_bytes of this DownloadAttachmentDto.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this DownloadAttachmentDto.

        Size in bytes of attachment  # noqa: E501

        :param size_bytes: The size_bytes of this DownloadAttachmentDto.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

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
        if not isinstance(other, DownloadAttachmentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DownloadAttachmentDto):
            return True

        return self.to_dict() != other.to_dict()
