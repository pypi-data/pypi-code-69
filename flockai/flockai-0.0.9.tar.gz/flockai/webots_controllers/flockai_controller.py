import abc


class FlockAIController(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, config):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError

