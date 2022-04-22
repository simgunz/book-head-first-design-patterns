from bevarages import Bevarage


class CondimentDecorator(Bevarage):
    def __init__(self, bevarage):
        self._bevarage = bevarage
