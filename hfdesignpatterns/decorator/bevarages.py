import abc


class Bevarage(abc.ABC):
    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abc.abstractmethod
    def cost(self):
        raise NotImplementedError()
