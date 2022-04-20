import abc

from observer import Observer


class DisplayElement(abc.ABC):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self):
        self.temperature = None
        self.humidity = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}%"
            " humidity"
        )
