import abc


class Bevarage(abc.ABC):
    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abc.abstractmethod
    def cost(self):
        raise NotImplementedError()


class Espresso(Bevarage):
    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return 1.99


class DarkRoast(Bevarage):
    def __init__(self):
        self._description = "Dark Roast"

    def cost(self):
        return 0.99


class HouseBlend(Bevarage):
    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return 0.89
