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


class Email(object):
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
        'analysis': 'EmailAnalysis',
        'attachments': 'list[str]',
        'bcc': 'list[str]',
        'body': 'str',
        'body_md5_hash': 'str',
        'cc': 'list[str]',
        'charset': 'str',
        'created_at': 'datetime',
        '_from': 'str',
        'headers': 'dict(str, str)',
        'id': 'str',
        'inbox_id': 'str',
        'is_html': 'bool',
        'read': 'bool',
        'subject': 'str',
        'to': 'list[str]',
        'updated_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'analysis': 'analysis',
        'attachments': 'attachments',
        'bcc': 'bcc',
        'body': 'body',
        'body_md5_hash': 'bodyMD5Hash',
        'cc': 'cc',
        'charset': 'charset',
        'created_at': 'createdAt',
        '_from': 'from',
        'headers': 'headers',
        'id': 'id',
        'inbox_id': 'inboxId',
        'is_html': 'isHTML',
        'read': 'read',
        'subject': 'subject',
        'to': 'to',
        'updated_at': 'updatedAt',
        'user_id': 'userId'
    }

    def __init__(self, analysis=None, attachments=None, bcc=None, body=None, body_md5_hash=None, cc=None, charset=None, created_at=None, _from=None, headers=None, id=None, inbox_id=None, is_html=None, read=None, subject=None, to=None, updated_at=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """Email - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._analysis = None
        self._attachments = None
        self._bcc = None
        self._body = None
        self._body_md5_hash = None
        self._cc = None
        self._charset = None
        self._created_at = None
        self.__from = None
        self._headers = None
        self._id = None
        self._inbox_id = None
        self._is_html = None
        self._read = None
        self._subject = None
        self._to = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None

        if analysis is not None:
            self.analysis = analysis
        if attachments is not None:
            self.attachments = attachments
        if bcc is not None:
            self.bcc = bcc
        if body is not None:
            self.body = body
        if body_md5_hash is not None:
            self.body_md5_hash = body_md5_hash
        if cc is not None:
            self.cc = cc
        if charset is not None:
            self.charset = charset
        if created_at is not None:
            self.created_at = created_at
        if _from is not None:
            self._from = _from
        if headers is not None:
            self.headers = headers
        if id is not None:
            self.id = id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if is_html is not None:
            self.is_html = is_html
        if read is not None:
            self.read = read
        if subject is not None:
            self.subject = subject
        if to is not None:
            self.to = to
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def analysis(self):
        """Gets the analysis of this Email.  # noqa: E501


        :return: The analysis of this Email.  # noqa: E501
        :rtype: EmailAnalysis
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this Email.


        :param analysis: The analysis of this Email.  # noqa: E501
        :type: EmailAnalysis
        """

        self._analysis = analysis

    @property
    def attachments(self):
        """Gets the attachments of this Email.  # noqa: E501

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :return: The attachments of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Email.

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :param attachments: The attachments of this Email.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def bcc(self):
        """Gets the bcc of this Email.  # noqa: E501

        List of `BCC` recipients email was addressed to  # noqa: E501

        :return: The bcc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this Email.

        List of `BCC` recipients email was addressed to  # noqa: E501

        :param bcc: The bcc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def body(self):
        """Gets the body of this Email.  # noqa: E501

        The body of the email message  # noqa: E501

        :return: The body of this Email.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Email.

        The body of the email message  # noqa: E501

        :param body: The body of this Email.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def body_md5_hash(self):
        """Gets the body_md5_hash of this Email.  # noqa: E501

        A hash signature of the email message  # noqa: E501

        :return: The body_md5_hash of this Email.  # noqa: E501
        :rtype: str
        """
        return self._body_md5_hash

    @body_md5_hash.setter
    def body_md5_hash(self, body_md5_hash):
        """Sets the body_md5_hash of this Email.

        A hash signature of the email message  # noqa: E501

        :param body_md5_hash: The body_md5_hash of this Email.  # noqa: E501
        :type: str
        """

        self._body_md5_hash = body_md5_hash

    @property
    def cc(self):
        """Gets the cc of this Email.  # noqa: E501

        List of `CC` recipients email was addressed to  # noqa: E501

        :return: The cc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this Email.

        List of `CC` recipients email was addressed to  # noqa: E501

        :param cc: The cc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def charset(self):
        """Gets the charset of this Email.  # noqa: E501

        Detected character set of the email body such as UTF-8  # noqa: E501

        :return: The charset of this Email.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this Email.

        Detected character set of the email body such as UTF-8  # noqa: E501

        :param charset: The charset of this Email.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def created_at(self):
        """Gets the created_at of this Email.  # noqa: E501

        When was the email received by MailSlurp  # noqa: E501

        :return: The created_at of this Email.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Email.

        When was the email received by MailSlurp  # noqa: E501

        :param created_at: The created_at of this Email.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def _from(self):
        """Gets the _from of this Email.  # noqa: E501

        Who the email was sent from  # noqa: E501

        :return: The _from of this Email.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Email.

        Who the email was sent from  # noqa: E501

        :param _from: The _from of this Email.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def headers(self):
        """Gets the headers of this Email.  # noqa: E501


        :return: The headers of this Email.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Email.


        :param headers: The headers of this Email.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def id(self):
        """Gets the id of this Email.  # noqa: E501

        ID of the email  # noqa: E501

        :return: The id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Email.

        ID of the email  # noqa: E501

        :param id: The id of this Email.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this Email.  # noqa: E501

        ID of the inbox that received the email  # noqa: E501

        :return: The inbox_id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this Email.

        ID of the inbox that received the email  # noqa: E501

        :param inbox_id: The inbox_id of this Email.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def is_html(self):
        """Gets the is_html of this Email.  # noqa: E501

        Was HTML sent in the email body  # noqa: E501

        :return: The is_html of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this Email.

        Was HTML sent in the email body  # noqa: E501

        :param is_html: The is_html of this Email.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def read(self):
        """Gets the read of this Email.  # noqa: E501

        Has the email been viewed ever  # noqa: E501

        :return: The read of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this Email.

        Has the email been viewed ever  # noqa: E501

        :param read: The read of this Email.  # noqa: E501
        :type: bool
        """

        self._read = read

    @property
    def subject(self):
        """Gets the subject of this Email.  # noqa: E501

        The subject line of the email message  # noqa: E501

        :return: The subject of this Email.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Email.

        The subject line of the email message  # noqa: E501

        :param subject: The subject of this Email.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this Email.  # noqa: E501

        List of `To` recipients email was addressed to  # noqa: E501

        :return: The to of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Email.

        List of `To` recipients email was addressed to  # noqa: E501

        :param to: The to of this Email.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def updated_at(self):
        """Gets the updated_at of this Email.  # noqa: E501

        When was the email last updated  # noqa: E501

        :return: The updated_at of this Email.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Email.

        When was the email last updated  # noqa: E501

        :param updated_at: The updated_at of this Email.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this Email.  # noqa: E501

        ID of user that email belongs  # noqa: E501

        :return: The user_id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Email.

        ID of user that email belongs  # noqa: E501

        :param user_id: The user_id of this Email.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if not isinstance(other, Email):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Email):
            return True

        return self.to_dict() != other.to_dict()
