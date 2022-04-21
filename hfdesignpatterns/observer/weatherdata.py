from observer import Subject


class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def measurements_changed(self):
        """Called when the measurements change."""
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def set_measurements(self, temperature, humidity, pressure):
        """Method to simualte new measurements."""
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
