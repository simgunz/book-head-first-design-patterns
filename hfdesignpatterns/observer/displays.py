import abc

from observer import Observer


class DisplayElement(abc.ABC):
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}%"
            " humidity"
        )
