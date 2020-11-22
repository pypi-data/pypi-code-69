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


class PlayWP(object):
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
        'games_id': 'int',
        'play_id': 'int',
        'play_text': 'str',
        'home_id': 'int',
        'home': 'str',
        'away_id': 'int',
        'away': 'str',
        'spread': 'float',
        'home_ball': 'bool',
        'home_score': 'int',
        'away_score': 'int',
        'time_remaining': 'int',
        'yard_line': 'int',
        'down': 'int',
        'distance': 'int',
        'home_win_prob': 'float',
        'play_number': 'int'
    }

    attribute_map = {
        'games_id': 'gamesId',
        'play_id': 'playId',
        'play_text': 'playText',
        'home_id': 'homeId',
        'home': 'home',
        'away_id': 'awayId',
        'away': 'away',
        'spread': 'spread',
        'home_ball': 'homeBall',
        'home_score': 'homeScore',
        'away_score': 'awayScore',
        'time_remaining': 'timeRemaining',
        'yard_line': 'yardLine',
        'down': 'down',
        'distance': 'distance',
        'home_win_prob': 'homeWinProb',
        'play_number': 'playNumber'
    }

    def __init__(self, games_id=None, play_id=None, play_text=None, home_id=None, home=None, away_id=None, away=None, spread=None, home_ball=None, home_score=None, away_score=None, time_remaining=None, yard_line=None, down=None, distance=None, home_win_prob=None, play_number=None):  # noqa: E501
        """PlayWP - a model defined in Swagger"""  # noqa: E501

        self._games_id = None
        self._play_id = None
        self._play_text = None
        self._home_id = None
        self._home = None
        self._away_id = None
        self._away = None
        self._spread = None
        self._home_ball = None
        self._home_score = None
        self._away_score = None
        self._time_remaining = None
        self._yard_line = None
        self._down = None
        self._distance = None
        self._home_win_prob = None
        self._play_number = None
        self.discriminator = None

        if games_id is not None:
            self.games_id = games_id
        if play_id is not None:
            self.play_id = play_id
        if play_text is not None:
            self.play_text = play_text
        if home_id is not None:
            self.home_id = home_id
        if home is not None:
            self.home = home
        if away_id is not None:
            self.away_id = away_id
        if away is not None:
            self.away = away
        if spread is not None:
            self.spread = spread
        if home_ball is not None:
            self.home_ball = home_ball
        if home_score is not None:
            self.home_score = home_score
        if away_score is not None:
            self.away_score = away_score
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if yard_line is not None:
            self.yard_line = yard_line
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if home_win_prob is not None:
            self.home_win_prob = home_win_prob
        if play_number is not None:
            self.play_number = play_number

    @property
    def games_id(self):
        """Gets the games_id of this PlayWP.  # noqa: E501


        :return: The games_id of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._games_id

    @games_id.setter
    def games_id(self, games_id):
        """Sets the games_id of this PlayWP.


        :param games_id: The games_id of this PlayWP.  # noqa: E501
        :type: int
        """

        self._games_id = games_id

    @property
    def play_id(self):
        """Gets the play_id of this PlayWP.  # noqa: E501


        :return: The play_id of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._play_id

    @play_id.setter
    def play_id(self, play_id):
        """Sets the play_id of this PlayWP.


        :param play_id: The play_id of this PlayWP.  # noqa: E501
        :type: int
        """

        self._play_id = play_id

    @property
    def play_text(self):
        """Gets the play_text of this PlayWP.  # noqa: E501


        :return: The play_text of this PlayWP.  # noqa: E501
        :rtype: str
        """
        return self._play_text

    @play_text.setter
    def play_text(self, play_text):
        """Sets the play_text of this PlayWP.


        :param play_text: The play_text of this PlayWP.  # noqa: E501
        :type: str
        """

        self._play_text = play_text

    @property
    def home_id(self):
        """Gets the home_id of this PlayWP.  # noqa: E501


        :return: The home_id of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._home_id

    @home_id.setter
    def home_id(self, home_id):
        """Sets the home_id of this PlayWP.


        :param home_id: The home_id of this PlayWP.  # noqa: E501
        :type: int
        """

        self._home_id = home_id

    @property
    def home(self):
        """Gets the home of this PlayWP.  # noqa: E501


        :return: The home of this PlayWP.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this PlayWP.


        :param home: The home of this PlayWP.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def away_id(self):
        """Gets the away_id of this PlayWP.  # noqa: E501


        :return: The away_id of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._away_id

    @away_id.setter
    def away_id(self, away_id):
        """Sets the away_id of this PlayWP.


        :param away_id: The away_id of this PlayWP.  # noqa: E501
        :type: int
        """

        self._away_id = away_id

    @property
    def away(self):
        """Gets the away of this PlayWP.  # noqa: E501


        :return: The away of this PlayWP.  # noqa: E501
        :rtype: str
        """
        return self._away

    @away.setter
    def away(self, away):
        """Sets the away of this PlayWP.


        :param away: The away of this PlayWP.  # noqa: E501
        :type: str
        """

        self._away = away

    @property
    def spread(self):
        """Gets the spread of this PlayWP.  # noqa: E501


        :return: The spread of this PlayWP.  # noqa: E501
        :rtype: float
        """
        return self._spread

    @spread.setter
    def spread(self, spread):
        """Sets the spread of this PlayWP.


        :param spread: The spread of this PlayWP.  # noqa: E501
        :type: float
        """

        self._spread = spread

    @property
    def home_ball(self):
        """Gets the home_ball of this PlayWP.  # noqa: E501


        :return: The home_ball of this PlayWP.  # noqa: E501
        :rtype: bool
        """
        return self._home_ball

    @home_ball.setter
    def home_ball(self, home_ball):
        """Sets the home_ball of this PlayWP.


        :param home_ball: The home_ball of this PlayWP.  # noqa: E501
        :type: bool
        """

        self._home_ball = home_ball

    @property
    def home_score(self):
        """Gets the home_score of this PlayWP.  # noqa: E501


        :return: The home_score of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._home_score

    @home_score.setter
    def home_score(self, home_score):
        """Sets the home_score of this PlayWP.


        :param home_score: The home_score of this PlayWP.  # noqa: E501
        :type: int
        """

        self._home_score = home_score

    @property
    def away_score(self):
        """Gets the away_score of this PlayWP.  # noqa: E501


        :return: The away_score of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._away_score

    @away_score.setter
    def away_score(self, away_score):
        """Sets the away_score of this PlayWP.


        :param away_score: The away_score of this PlayWP.  # noqa: E501
        :type: int
        """

        self._away_score = away_score

    @property
    def time_remaining(self):
        """Gets the time_remaining of this PlayWP.  # noqa: E501


        :return: The time_remaining of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this PlayWP.


        :param time_remaining: The time_remaining of this PlayWP.  # noqa: E501
        :type: int
        """

        self._time_remaining = time_remaining

    @property
    def yard_line(self):
        """Gets the yard_line of this PlayWP.  # noqa: E501


        :return: The yard_line of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._yard_line

    @yard_line.setter
    def yard_line(self, yard_line):
        """Sets the yard_line of this PlayWP.


        :param yard_line: The yard_line of this PlayWP.  # noqa: E501
        :type: int
        """

        self._yard_line = yard_line

    @property
    def down(self):
        """Gets the down of this PlayWP.  # noqa: E501


        :return: The down of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this PlayWP.


        :param down: The down of this PlayWP.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this PlayWP.  # noqa: E501


        :return: The distance of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this PlayWP.


        :param distance: The distance of this PlayWP.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def home_win_prob(self):
        """Gets the home_win_prob of this PlayWP.  # noqa: E501


        :return: The home_win_prob of this PlayWP.  # noqa: E501
        :rtype: float
        """
        return self._home_win_prob

    @home_win_prob.setter
    def home_win_prob(self, home_win_prob):
        """Sets the home_win_prob of this PlayWP.


        :param home_win_prob: The home_win_prob of this PlayWP.  # noqa: E501
        :type: float
        """

        self._home_win_prob = home_win_prob

    @property
    def play_number(self):
        """Gets the play_number of this PlayWP.  # noqa: E501


        :return: The play_number of this PlayWP.  # noqa: E501
        :rtype: int
        """
        return self._play_number

    @play_number.setter
    def play_number(self, play_number):
        """Sets the play_number of this PlayWP.


        :param play_number: The play_number of this PlayWP.  # noqa: E501
        :type: int
        """

        self._play_number = play_number

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
        if issubclass(PlayWP, dict):
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
        if not isinstance(other, PlayWP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
