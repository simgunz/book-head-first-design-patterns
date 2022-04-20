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
        self.display()  # Not so nice to call display here

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}%"
            " humidity"
        )


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperatures = []
        self.min_temperature = 1000
        self.max_temperature = -1000
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.min_temperature = min(self.min_temperature, temperature)
        self.max_temperature = max(self.max_temperature, temperature)
        self.display()  # Not so nice to call display here

    def display(self):
        print(
            "Avg/Max/Min temperature ="
            f" {sum(self.temperatures) / len(self.temperatures)}"
            "/{self.max_temperature}/{self.min_temperature}"
        )
