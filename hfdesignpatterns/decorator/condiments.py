import abc

from bevarages import Bevarage


class CondimentDecorator(Bevarage):
    def __init__(self, bevarage):
        self._bevarage = bevarage

    @abc.abstractmethod
    def get_description(self):
        raise NotImplementedError()
