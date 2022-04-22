import abc


class CondimentDecorator(abc.ABC):
    def __init__(self, bevarage):
        self._bevarage = bevarage

    @abc.abstractmethod
    def get_description(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def cost(self):
        raise NotImplementedError()
