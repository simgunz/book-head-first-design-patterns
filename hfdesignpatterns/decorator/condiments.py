import abc

from bevarages import Bevarage


class CondimentDecorator(Bevarage):
    def __init__(self, bevarage):
        self._bevarage = bevarage

    @abc.abstractmethod
    def get_description(self):
        raise NotImplementedError()


class Mocha(CondimentDecorator):
    def get_description(self):
        return self._bevarage.get_description() + ", Mocha"

    def cost(self):
        return self._bevarage.cost() + 0.20


class Soy(CondimentDecorator):
    def get_description(self):
        return self._bevarage.get_description() + ", Soy"

    def cost(self):
        return self._bevarage.cost() + 0.15


class Whip(CondimentDecorator):
    def get_description(self):
        return self._bevarage.get_description() + ", Whip"

    def cost(self):
        return self._bevarage.cost() + 0.10
