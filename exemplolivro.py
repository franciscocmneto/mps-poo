
class Subject: #interface/classe abstrata
    def register_observer(self, Observer):
        pass

    def remove_observer(self, Observer):
        pass

    def notify_observer(self):
        pass


class Observer:
    def update(self, temperature, humidity, pressure):
        pass


class DisplayElement:
    def display(self):
        pass


class WeatherData (Subject):
    def __init__(self):
        self.__observers =[]
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None

    def register_observer(self, Observer):
        self.__observers.append(Observer)

    def remove_observer(self, Observer):
        try:
            self.__observers.remove(Observer)
        except:
            pass

    def notify_observer(self):
        for observer in self.__observers:
            observer.update(self.__temperature,self.__humidity,self.__pressure)


    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature,humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

        self.measurements_changed()

class current_conditions_display(Observer,DisplayElement):

    def __init__(self, weather_data):
        self.__temperature = None
        self.__humidity = None
        self.__weather_data = weather_data

        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.display()

    def display(self):
        print("Current conditions " + str(self.__temperature)+"F degrees and " + str(self.__humidity)+ " % humidity")


if __name__ == '__main__':
    weather_data = WeatherData()

    current_display = current_conditions_display(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)