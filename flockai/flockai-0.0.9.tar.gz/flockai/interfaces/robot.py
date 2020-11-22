import abc
from controller import Robot


class IRobot(Robot):
    """
    Inherit functionalities provided by the Webots Robot library and declare abstract methods
    """
    def __init__(self):
        super(IRobot).__init__()

    @abc.abstractmethod
    def initialize(self):
        """
        The actions needed to initialize a drone
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _attach_and_enable_devices(self):
        """
        Attach and enable the devices on a drone
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _attach_and_enable_motors(self):
        """
        Attach and enable the motors on a drone
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _set_variables(self):
        """
        Set variables needed for controlling the drone on air
        :return:
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _set_constants(self):
        """
        Set constants needed for controlling the drone on air
        :return:
        """
        raise NotImplementedError
