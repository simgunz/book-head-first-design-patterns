from displays import CurrentConditionsDisplay, StatisticsDisplay
from weatherdata import WeatherData


def main():
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)


if __name__ == "__main__":
    main()
