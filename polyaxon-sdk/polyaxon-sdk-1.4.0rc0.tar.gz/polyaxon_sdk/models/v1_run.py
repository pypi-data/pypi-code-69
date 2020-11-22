#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.4.0-rc0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1Run(object):
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
        'uuid': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'user': 'str',
        'owner': 'str',
        'project': 'str',
        'schedule_at': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'duration': 'int',
        'is_managed': 'bool',
        'is_approved': 'bool',
        'content': 'str',
        'raw_content': 'str',
        'status': 'V1Statuses',
        'bookmarked': 'bool',
        'meta_info': 'object',
        'kind': 'V1RunKind',
        'runtime': 'V1RunKind',
        'hub': 'str',
        'inputs': 'object',
        'outputs': 'object',
        'original': 'V1Cloning',
        'pipeline': 'V1Pipeline',
        'status_conditions': 'list[V1StatusCondition]',
        'settings': 'V1RunSettings',
        'role': 'str',
        'live_state': 'int'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'user': 'user',
        'owner': 'owner',
        'project': 'project',
        'schedule_at': 'schedule_at',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'duration': 'duration',
        'is_managed': 'is_managed',
        'is_approved': 'is_approved',
        'content': 'content',
        'raw_content': 'raw_content',
        'status': 'status',
        'bookmarked': 'bookmarked',
        'meta_info': 'meta_info',
        'kind': 'kind',
        'runtime': 'runtime',
        'hub': 'hub',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'original': 'original',
        'pipeline': 'pipeline',
        'status_conditions': 'status_conditions',
        'settings': 'settings',
        'role': 'role',
        'live_state': 'live_state'
    }

    def __init__(self, uuid=None, name=None, description=None, tags=None, user=None, owner=None, project=None, schedule_at=None, created_at=None, updated_at=None, started_at=None, finished_at=None, duration=None, is_managed=None, is_approved=None, content=None, raw_content=None, status=None, bookmarked=None, meta_info=None, kind=None, runtime=None, hub=None, inputs=None, outputs=None, original=None, pipeline=None, status_conditions=None, settings=None, role=None, live_state=None, local_vars_configuration=None):  # noqa: E501
        """V1Run - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._name = None
        self._description = None
        self._tags = None
        self._user = None
        self._owner = None
        self._project = None
        self._schedule_at = None
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._finished_at = None
        self._duration = None
        self._is_managed = None
        self._is_approved = None
        self._content = None
        self._raw_content = None
        self._status = None
        self._bookmarked = None
        self._meta_info = None
        self._kind = None
        self._runtime = None
        self._hub = None
        self._inputs = None
        self._outputs = None
        self._original = None
        self._pipeline = None
        self._status_conditions = None
        self._settings = None
        self._role = None
        self._live_state = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if user is not None:
            self.user = user
        if owner is not None:
            self.owner = owner
        if project is not None:
            self.project = project
        if schedule_at is not None:
            self.schedule_at = schedule_at
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if duration is not None:
            self.duration = duration
        if is_managed is not None:
            self.is_managed = is_managed
        if is_approved is not None:
            self.is_approved = is_approved
        if content is not None:
            self.content = content
        if raw_content is not None:
            self.raw_content = raw_content
        if status is not None:
            self.status = status
        if bookmarked is not None:
            self.bookmarked = bookmarked
        if meta_info is not None:
            self.meta_info = meta_info
        if kind is not None:
            self.kind = kind
        if runtime is not None:
            self.runtime = runtime
        if hub is not None:
            self.hub = hub
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if original is not None:
            self.original = original
        if pipeline is not None:
            self.pipeline = pipeline
        if status_conditions is not None:
            self.status_conditions = status_conditions
        if settings is not None:
            self.settings = settings
        if role is not None:
            self.role = role
        if live_state is not None:
            self.live_state = live_state

    @property
    def uuid(self):
        """Gets the uuid of this V1Run.  # noqa: E501


        :return: The uuid of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1Run.


        :param uuid: The uuid of this V1Run.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this V1Run.  # noqa: E501


        :return: The name of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Run.


        :param name: The name of this V1Run.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1Run.  # noqa: E501


        :return: The description of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1Run.


        :param description: The description of this V1Run.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this V1Run.  # noqa: E501


        :return: The tags of this V1Run.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1Run.


        :param tags: The tags of this V1Run.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def user(self):
        """Gets the user of this V1Run.  # noqa: E501


        :return: The user of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1Run.


        :param user: The user of this V1Run.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def owner(self):
        """Gets the owner of this V1Run.  # noqa: E501


        :return: The owner of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this V1Run.


        :param owner: The owner of this V1Run.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def project(self):
        """Gets the project of this V1Run.  # noqa: E501


        :return: The project of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1Run.


        :param project: The project of this V1Run.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def schedule_at(self):
        """Gets the schedule_at of this V1Run.  # noqa: E501


        :return: The schedule_at of this V1Run.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_at

    @schedule_at.setter
    def schedule_at(self, schedule_at):
        """Sets the schedule_at of this V1Run.


        :param schedule_at: The schedule_at of this V1Run.  # noqa: E501
        :type: datetime
        """

        self._schedule_at = schedule_at

    @property
    def created_at(self):
        """Gets the created_at of this V1Run.  # noqa: E501


        :return: The created_at of this V1Run.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1Run.


        :param created_at: The created_at of this V1Run.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this V1Run.  # noqa: E501


        :return: The updated_at of this V1Run.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V1Run.


        :param updated_at: The updated_at of this V1Run.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def started_at(self):
        """Gets the started_at of this V1Run.  # noqa: E501


        :return: The started_at of this V1Run.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this V1Run.


        :param started_at: The started_at of this V1Run.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this V1Run.  # noqa: E501


        :return: The finished_at of this V1Run.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this V1Run.


        :param finished_at: The finished_at of this V1Run.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def duration(self):
        """Gets the duration of this V1Run.  # noqa: E501


        :return: The duration of this V1Run.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this V1Run.


        :param duration: The duration of this V1Run.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def is_managed(self):
        """Gets the is_managed of this V1Run.  # noqa: E501


        :return: The is_managed of this V1Run.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this V1Run.


        :param is_managed: The is_managed of this V1Run.  # noqa: E501
        :type: bool
        """

        self._is_managed = is_managed

    @property
    def is_approved(self):
        """Gets the is_approved of this V1Run.  # noqa: E501


        :return: The is_approved of this V1Run.  # noqa: E501
        :rtype: bool
        """
        return self._is_approved

    @is_approved.setter
    def is_approved(self, is_approved):
        """Sets the is_approved of this V1Run.


        :param is_approved: The is_approved of this V1Run.  # noqa: E501
        :type: bool
        """

        self._is_approved = is_approved

    @property
    def content(self):
        """Gets the content of this V1Run.  # noqa: E501


        :return: The content of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V1Run.


        :param content: The content of this V1Run.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def raw_content(self):
        """Gets the raw_content of this V1Run.  # noqa: E501


        :return: The raw_content of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._raw_content

    @raw_content.setter
    def raw_content(self, raw_content):
        """Sets the raw_content of this V1Run.


        :param raw_content: The raw_content of this V1Run.  # noqa: E501
        :type: str
        """

        self._raw_content = raw_content

    @property
    def status(self):
        """Gets the status of this V1Run.  # noqa: E501


        :return: The status of this V1Run.  # noqa: E501
        :rtype: V1Statuses
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1Run.


        :param status: The status of this V1Run.  # noqa: E501
        :type: V1Statuses
        """

        self._status = status

    @property
    def bookmarked(self):
        """Gets the bookmarked of this V1Run.  # noqa: E501


        :return: The bookmarked of this V1Run.  # noqa: E501
        :rtype: bool
        """
        return self._bookmarked

    @bookmarked.setter
    def bookmarked(self, bookmarked):
        """Sets the bookmarked of this V1Run.


        :param bookmarked: The bookmarked of this V1Run.  # noqa: E501
        :type: bool
        """

        self._bookmarked = bookmarked

    @property
    def meta_info(self):
        """Gets the meta_info of this V1Run.  # noqa: E501


        :return: The meta_info of this V1Run.  # noqa: E501
        :rtype: object
        """
        return self._meta_info

    @meta_info.setter
    def meta_info(self, meta_info):
        """Sets the meta_info of this V1Run.


        :param meta_info: The meta_info of this V1Run.  # noqa: E501
        :type: object
        """

        self._meta_info = meta_info

    @property
    def kind(self):
        """Gets the kind of this V1Run.  # noqa: E501


        :return: The kind of this V1Run.  # noqa: E501
        :rtype: V1RunKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Run.


        :param kind: The kind of this V1Run.  # noqa: E501
        :type: V1RunKind
        """

        self._kind = kind

    @property
    def runtime(self):
        """Gets the runtime of this V1Run.  # noqa: E501


        :return: The runtime of this V1Run.  # noqa: E501
        :rtype: V1RunKind
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this V1Run.


        :param runtime: The runtime of this V1Run.  # noqa: E501
        :type: V1RunKind
        """

        self._runtime = runtime

    @property
    def hub(self):
        """Gets the hub of this V1Run.  # noqa: E501


        :return: The hub of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._hub

    @hub.setter
    def hub(self, hub):
        """Sets the hub of this V1Run.


        :param hub: The hub of this V1Run.  # noqa: E501
        :type: str
        """

        self._hub = hub

    @property
    def inputs(self):
        """Gets the inputs of this V1Run.  # noqa: E501


        :return: The inputs of this V1Run.  # noqa: E501
        :rtype: object
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this V1Run.


        :param inputs: The inputs of this V1Run.  # noqa: E501
        :type: object
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this V1Run.  # noqa: E501


        :return: The outputs of this V1Run.  # noqa: E501
        :rtype: object
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this V1Run.


        :param outputs: The outputs of this V1Run.  # noqa: E501
        :type: object
        """

        self._outputs = outputs

    @property
    def original(self):
        """Gets the original of this V1Run.  # noqa: E501


        :return: The original of this V1Run.  # noqa: E501
        :rtype: V1Cloning
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this V1Run.


        :param original: The original of this V1Run.  # noqa: E501
        :type: V1Cloning
        """

        self._original = original

    @property
    def pipeline(self):
        """Gets the pipeline of this V1Run.  # noqa: E501


        :return: The pipeline of this V1Run.  # noqa: E501
        :rtype: V1Pipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this V1Run.


        :param pipeline: The pipeline of this V1Run.  # noqa: E501
        :type: V1Pipeline
        """

        self._pipeline = pipeline

    @property
    def status_conditions(self):
        """Gets the status_conditions of this V1Run.  # noqa: E501


        :return: The status_conditions of this V1Run.  # noqa: E501
        :rtype: list[V1StatusCondition]
        """
        return self._status_conditions

    @status_conditions.setter
    def status_conditions(self, status_conditions):
        """Sets the status_conditions of this V1Run.


        :param status_conditions: The status_conditions of this V1Run.  # noqa: E501
        :type: list[V1StatusCondition]
        """

        self._status_conditions = status_conditions

    @property
    def settings(self):
        """Gets the settings of this V1Run.  # noqa: E501


        :return: The settings of this V1Run.  # noqa: E501
        :rtype: V1RunSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this V1Run.


        :param settings: The settings of this V1Run.  # noqa: E501
        :type: V1RunSettings
        """

        self._settings = settings

    @property
    def role(self):
        """Gets the role of this V1Run.  # noqa: E501


        :return: The role of this V1Run.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V1Run.


        :param role: The role of this V1Run.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def live_state(self):
        """Gets the live_state of this V1Run.  # noqa: E501


        :return: The live_state of this V1Run.  # noqa: E501
        :rtype: int
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        """Sets the live_state of this V1Run.


        :param live_state: The live_state of this V1Run.  # noqa: E501
        :type: int
        """

        self._live_state = live_state

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
        if not isinstance(other, V1Run):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Run):
            return True

        return self.to_dict() != other.to_dict()
