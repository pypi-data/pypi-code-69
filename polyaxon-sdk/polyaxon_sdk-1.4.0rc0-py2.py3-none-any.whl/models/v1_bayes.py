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


class V1Bayes(object):
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
        'kind': 'str',
        'params': 'dict(str, object)',
        'num_initial_runs': 'int',
        'max_iterations': 'int',
        'utility_function': 'object',
        'metric': 'V1OptimizationMetric',
        'seed': 'int',
        'concurrency': 'int',
        'container': 'V1Container',
        'early_stopping': 'list[object]'
    }

    attribute_map = {
        'kind': 'kind',
        'params': 'params',
        'num_initial_runs': 'num_initial_runs',
        'max_iterations': 'max_iterations',
        'utility_function': 'utility_function',
        'metric': 'metric',
        'seed': 'seed',
        'concurrency': 'concurrency',
        'container': 'container',
        'early_stopping': 'early_stopping'
    }

    def __init__(self, kind='bayes', params=None, num_initial_runs=None, max_iterations=None, utility_function=None, metric=None, seed=None, concurrency=None, container=None, early_stopping=None, local_vars_configuration=None):  # noqa: E501
        """V1Bayes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kind = None
        self._params = None
        self._num_initial_runs = None
        self._max_iterations = None
        self._utility_function = None
        self._metric = None
        self._seed = None
        self._concurrency = None
        self._container = None
        self._early_stopping = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if params is not None:
            self.params = params
        if num_initial_runs is not None:
            self.num_initial_runs = num_initial_runs
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if utility_function is not None:
            self.utility_function = utility_function
        if metric is not None:
            self.metric = metric
        if seed is not None:
            self.seed = seed
        if concurrency is not None:
            self.concurrency = concurrency
        if container is not None:
            self.container = container
        if early_stopping is not None:
            self.early_stopping = early_stopping

    @property
    def kind(self):
        """Gets the kind of this V1Bayes.  # noqa: E501


        :return: The kind of this V1Bayes.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Bayes.


        :param kind: The kind of this V1Bayes.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def params(self):
        """Gets the params of this V1Bayes.  # noqa: E501


        :return: The params of this V1Bayes.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this V1Bayes.


        :param params: The params of this V1Bayes.  # noqa: E501
        :type: dict(str, object)
        """

        self._params = params

    @property
    def num_initial_runs(self):
        """Gets the num_initial_runs of this V1Bayes.  # noqa: E501


        :return: The num_initial_runs of this V1Bayes.  # noqa: E501
        :rtype: int
        """
        return self._num_initial_runs

    @num_initial_runs.setter
    def num_initial_runs(self, num_initial_runs):
        """Sets the num_initial_runs of this V1Bayes.


        :param num_initial_runs: The num_initial_runs of this V1Bayes.  # noqa: E501
        :type: int
        """

        self._num_initial_runs = num_initial_runs

    @property
    def max_iterations(self):
        """Gets the max_iterations of this V1Bayes.  # noqa: E501


        :return: The max_iterations of this V1Bayes.  # noqa: E501
        :rtype: int
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        """Sets the max_iterations of this V1Bayes.


        :param max_iterations: The max_iterations of this V1Bayes.  # noqa: E501
        :type: int
        """

        self._max_iterations = max_iterations

    @property
    def utility_function(self):
        """Gets the utility_function of this V1Bayes.  # noqa: E501


        :return: The utility_function of this V1Bayes.  # noqa: E501
        :rtype: object
        """
        return self._utility_function

    @utility_function.setter
    def utility_function(self, utility_function):
        """Sets the utility_function of this V1Bayes.


        :param utility_function: The utility_function of this V1Bayes.  # noqa: E501
        :type: object
        """

        self._utility_function = utility_function

    @property
    def metric(self):
        """Gets the metric of this V1Bayes.  # noqa: E501


        :return: The metric of this V1Bayes.  # noqa: E501
        :rtype: V1OptimizationMetric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this V1Bayes.


        :param metric: The metric of this V1Bayes.  # noqa: E501
        :type: V1OptimizationMetric
        """

        self._metric = metric

    @property
    def seed(self):
        """Gets the seed of this V1Bayes.  # noqa: E501


        :return: The seed of this V1Bayes.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this V1Bayes.


        :param seed: The seed of this V1Bayes.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def concurrency(self):
        """Gets the concurrency of this V1Bayes.  # noqa: E501


        :return: The concurrency of this V1Bayes.  # noqa: E501
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this V1Bayes.


        :param concurrency: The concurrency of this V1Bayes.  # noqa: E501
        :type: int
        """

        self._concurrency = concurrency

    @property
    def container(self):
        """Gets the container of this V1Bayes.  # noqa: E501


        :return: The container of this V1Bayes.  # noqa: E501
        :rtype: V1Container
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this V1Bayes.


        :param container: The container of this V1Bayes.  # noqa: E501
        :type: V1Container
        """

        self._container = container

    @property
    def early_stopping(self):
        """Gets the early_stopping of this V1Bayes.  # noqa: E501


        :return: The early_stopping of this V1Bayes.  # noqa: E501
        :rtype: list[object]
        """
        return self._early_stopping

    @early_stopping.setter
    def early_stopping(self, early_stopping):
        """Sets the early_stopping of this V1Bayes.


        :param early_stopping: The early_stopping of this V1Bayes.  # noqa: E501
        :type: list[object]
        """

        self._early_stopping = early_stopping

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
        if not isinstance(other, V1Bayes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Bayes):
            return True

        return self.to_dict() != other.to_dict()
