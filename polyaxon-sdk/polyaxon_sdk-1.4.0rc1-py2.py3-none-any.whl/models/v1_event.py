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

    The version of the OpenAPI document: 1.4.0-rc1
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1Event(object):
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
        'timestamp': 'datetime',
        'step': 'int',
        'metric': 'float',
        'image': 'V1EventImage',
        'histogram': 'V1EventHistogram',
        'audio': 'V1EventAudio',
        'video': 'V1EventVideo',
        'html': 'str',
        'text': 'str',
        'chart': 'V1EventChart',
        'model': 'V1EventModel',
        'artifact': 'V1EventArtifact',
        'dataframe': 'V1EventDataframe',
        'curve': 'V1EventCurve'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'step': 'step',
        'metric': 'metric',
        'image': 'image',
        'histogram': 'histogram',
        'audio': 'audio',
        'video': 'video',
        'html': 'html',
        'text': 'text',
        'chart': 'chart',
        'model': 'model',
        'artifact': 'artifact',
        'dataframe': 'dataframe',
        'curve': 'curve'
    }

    def __init__(self, timestamp=None, step=None, metric=None, image=None, histogram=None, audio=None, video=None, html=None, text=None, chart=None, model=None, artifact=None, dataframe=None, curve=None, local_vars_configuration=None):  # noqa: E501
        """V1Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._step = None
        self._metric = None
        self._image = None
        self._histogram = None
        self._audio = None
        self._video = None
        self._html = None
        self._text = None
        self._chart = None
        self._model = None
        self._artifact = None
        self._dataframe = None
        self._curve = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if step is not None:
            self.step = step
        if metric is not None:
            self.metric = metric
        if image is not None:
            self.image = image
        if histogram is not None:
            self.histogram = histogram
        if audio is not None:
            self.audio = audio
        if video is not None:
            self.video = video
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if chart is not None:
            self.chart = chart
        if model is not None:
            self.model = model
        if artifact is not None:
            self.artifact = artifact
        if dataframe is not None:
            self.dataframe = dataframe
        if curve is not None:
            self.curve = curve

    @property
    def timestamp(self):
        """Gets the timestamp of this V1Event.  # noqa: E501


        :return: The timestamp of this V1Event.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this V1Event.


        :param timestamp: The timestamp of this V1Event.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def step(self):
        """Gets the step of this V1Event.  # noqa: E501

        Global step of the event.  # noqa: E501

        :return: The step of this V1Event.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this V1Event.

        Global step of the event.  # noqa: E501

        :param step: The step of this V1Event.  # noqa: E501
        :type: int
        """

        self._step = step

    @property
    def metric(self):
        """Gets the metric of this V1Event.  # noqa: E501


        :return: The metric of this V1Event.  # noqa: E501
        :rtype: float
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this V1Event.


        :param metric: The metric of this V1Event.  # noqa: E501
        :type: float
        """

        self._metric = metric

    @property
    def image(self):
        """Gets the image of this V1Event.  # noqa: E501


        :return: The image of this V1Event.  # noqa: E501
        :rtype: V1EventImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1Event.


        :param image: The image of this V1Event.  # noqa: E501
        :type: V1EventImage
        """

        self._image = image

    @property
    def histogram(self):
        """Gets the histogram of this V1Event.  # noqa: E501


        :return: The histogram of this V1Event.  # noqa: E501
        :rtype: V1EventHistogram
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this V1Event.


        :param histogram: The histogram of this V1Event.  # noqa: E501
        :type: V1EventHistogram
        """

        self._histogram = histogram

    @property
    def audio(self):
        """Gets the audio of this V1Event.  # noqa: E501


        :return: The audio of this V1Event.  # noqa: E501
        :rtype: V1EventAudio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this V1Event.


        :param audio: The audio of this V1Event.  # noqa: E501
        :type: V1EventAudio
        """

        self._audio = audio

    @property
    def video(self):
        """Gets the video of this V1Event.  # noqa: E501


        :return: The video of this V1Event.  # noqa: E501
        :rtype: V1EventVideo
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this V1Event.


        :param video: The video of this V1Event.  # noqa: E501
        :type: V1EventVideo
        """

        self._video = video

    @property
    def html(self):
        """Gets the html of this V1Event.  # noqa: E501


        :return: The html of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this V1Event.


        :param html: The html of this V1Event.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this V1Event.  # noqa: E501


        :return: The text of this V1Event.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this V1Event.


        :param text: The text of this V1Event.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def chart(self):
        """Gets the chart of this V1Event.  # noqa: E501


        :return: The chart of this V1Event.  # noqa: E501
        :rtype: V1EventChart
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        """Sets the chart of this V1Event.


        :param chart: The chart of this V1Event.  # noqa: E501
        :type: V1EventChart
        """

        self._chart = chart

    @property
    def model(self):
        """Gets the model of this V1Event.  # noqa: E501


        :return: The model of this V1Event.  # noqa: E501
        :rtype: V1EventModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this V1Event.


        :param model: The model of this V1Event.  # noqa: E501
        :type: V1EventModel
        """

        self._model = model

    @property
    def artifact(self):
        """Gets the artifact of this V1Event.  # noqa: E501


        :return: The artifact of this V1Event.  # noqa: E501
        :rtype: V1EventArtifact
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this V1Event.


        :param artifact: The artifact of this V1Event.  # noqa: E501
        :type: V1EventArtifact
        """

        self._artifact = artifact

    @property
    def dataframe(self):
        """Gets the dataframe of this V1Event.  # noqa: E501


        :return: The dataframe of this V1Event.  # noqa: E501
        :rtype: V1EventDataframe
        """
        return self._dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        """Sets the dataframe of this V1Event.


        :param dataframe: The dataframe of this V1Event.  # noqa: E501
        :type: V1EventDataframe
        """

        self._dataframe = dataframe

    @property
    def curve(self):
        """Gets the curve of this V1Event.  # noqa: E501


        :return: The curve of this V1Event.  # noqa: E501
        :rtype: V1EventCurve
        """
        return self._curve

    @curve.setter
    def curve(self, curve):
        """Sets the curve of this V1Event.


        :param curve: The curve of this V1Event.  # noqa: E501
        :type: V1EventCurve
        """

        self._curve = curve

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
        if not isinstance(other, V1Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Event):
            return True

        return self.to_dict() != other.to_dict()
