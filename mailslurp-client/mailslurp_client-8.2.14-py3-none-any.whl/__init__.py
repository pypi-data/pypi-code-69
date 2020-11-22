# coding: utf-8

# flake8: noqa

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "8.2.14"

# import apis into sdk package
from mailslurp_client.api.alias_controller_api import AliasControllerApi
from mailslurp_client.api.attachment_controller_api import AttachmentControllerApi
from mailslurp_client.api.bulk_actions_controller_api import BulkActionsControllerApi
from mailslurp_client.api.common_actions_controller_api import CommonActionsControllerApi
from mailslurp_client.api.contact_controller_api import ContactControllerApi
from mailslurp_client.api.domain_controller_api import DomainControllerApi
from mailslurp_client.api.email_controller_api import EmailControllerApi
from mailslurp_client.api.form_controller_api import FormControllerApi
from mailslurp_client.api.group_controller_api import GroupControllerApi
from mailslurp_client.api.inbox_controller_api import InboxControllerApi
from mailslurp_client.api.mail_server_controller_api import MailServerControllerApi
from mailslurp_client.api.sent_emails_controller_api import SentEmailsControllerApi
from mailslurp_client.api.template_controller_api import TemplateControllerApi
from mailslurp_client.api.wait_for_controller_api import WaitForControllerApi
from mailslurp_client.api.webhook_controller_api import WebhookControllerApi

# import ApiClient
from mailslurp_client.api_client import ApiClient
from mailslurp_client.configuration import Configuration
from mailslurp_client.exceptions import OpenApiException
from mailslurp_client.exceptions import ApiTypeError
from mailslurp_client.exceptions import ApiValueError
from mailslurp_client.exceptions import ApiKeyError
from mailslurp_client.exceptions import ApiException
# import models into sdk package
from mailslurp_client.models.alias import Alias
from mailslurp_client.models.attachment_meta_data import AttachmentMetaData
from mailslurp_client.models.basic_auth_options import BasicAuthOptions
from mailslurp_client.models.bulk_send_email_options import BulkSendEmailOptions
from mailslurp_client.models.contact_dto import ContactDto
from mailslurp_client.models.contact_projection import ContactProjection
from mailslurp_client.models.content_match_options import ContentMatchOptions
from mailslurp_client.models.create_anonymous_alias_options import CreateAnonymousAliasOptions
from mailslurp_client.models.create_contact_options import CreateContactOptions
from mailslurp_client.models.create_domain_options import CreateDomainOptions
from mailslurp_client.models.create_group_options import CreateGroupOptions
from mailslurp_client.models.create_owned_alias_options import CreateOwnedAliasOptions
from mailslurp_client.models.create_template_options import CreateTemplateOptions
from mailslurp_client.models.create_webhook_options import CreateWebhookOptions
from mailslurp_client.models.describe_domain_options import DescribeDomainOptions
from mailslurp_client.models.describe_mail_server_domain_result import DescribeMailServerDomainResult
from mailslurp_client.models.domain_dto import DomainDto
from mailslurp_client.models.domain_preview import DomainPreview
from mailslurp_client.models.download_attachment_dto import DownloadAttachmentDto
from mailslurp_client.models.email import Email
from mailslurp_client.models.email_analysis import EmailAnalysis
from mailslurp_client.models.email_content_match_result import EmailContentMatchResult
from mailslurp_client.models.email_preview import EmailPreview
from mailslurp_client.models.email_projection import EmailProjection
from mailslurp_client.models.email_verification_result import EmailVerificationResult
from mailslurp_client.models.forward_email_options import ForwardEmailOptions
from mailslurp_client.models.group_contacts_dto import GroupContactsDto
from mailslurp_client.models.group_dto import GroupDto
from mailslurp_client.models.group_projection import GroupProjection
from mailslurp_client.models.html_validation_result import HTMLValidationResult
from mailslurp_client.models.inbox import Inbox
from mailslurp_client.models.inbox_projection import InboxProjection
from mailslurp_client.models.match_option import MatchOption
from mailslurp_client.models.match_options import MatchOptions
from mailslurp_client.models.name_server_record import NameServerRecord
from mailslurp_client.models.page_alias import PageAlias
from mailslurp_client.models.page_contact_projection import PageContactProjection
from mailslurp_client.models.page_email_preview import PageEmailPreview
from mailslurp_client.models.page_email_projection import PageEmailProjection
from mailslurp_client.models.page_group_projection import PageGroupProjection
from mailslurp_client.models.page_inbox_projection import PageInboxProjection
from mailslurp_client.models.page_sent_email_projection import PageSentEmailProjection
from mailslurp_client.models.page_template_projection import PageTemplateProjection
from mailslurp_client.models.page_webhook_projection import PageWebhookProjection
from mailslurp_client.models.pageable import Pageable
from mailslurp_client.models.raw_email_json import RawEmailJson
from mailslurp_client.models.send_email_options import SendEmailOptions
from mailslurp_client.models.sent_email_dto import SentEmailDto
from mailslurp_client.models.sent_email_projection import SentEmailProjection
from mailslurp_client.models.set_inbox_favourited_options import SetInboxFavouritedOptions
from mailslurp_client.models.simple_send_email_options import SimpleSendEmailOptions
from mailslurp_client.models.sort import Sort
from mailslurp_client.models.template_dto import TemplateDto
from mailslurp_client.models.template_projection import TemplateProjection
from mailslurp_client.models.template_variable import TemplateVariable
from mailslurp_client.models.unread_count import UnreadCount
from mailslurp_client.models.update_group_contacts import UpdateGroupContacts
from mailslurp_client.models.update_inbox_options import UpdateInboxOptions
from mailslurp_client.models.upload_attachment_options import UploadAttachmentOptions
from mailslurp_client.models.validation_dto import ValidationDto
from mailslurp_client.models.validation_message import ValidationMessage
from mailslurp_client.models.verify_email_address_options import VerifyEmailAddressOptions
from mailslurp_client.models.wait_for_conditions import WaitForConditions
from mailslurp_client.models.webhook_dto import WebhookDto
from mailslurp_client.models.webhook_projection import WebhookProjection
from mailslurp_client.models.webhook_test_request import WebhookTestRequest
from mailslurp_client.models.webhook_test_response import WebhookTestResponse
from mailslurp_client.models.webhook_test_result import WebhookTestResult

