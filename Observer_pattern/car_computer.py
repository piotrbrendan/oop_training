class CarComputer(object):


    def __init__(self, start_temp):

        self.__is_awake = False
        self.observers = []
        self.__temperature = start_temp


    def add_observer(self, observer):
        self.observers.append(observer)

    def _update_observers(self):
        for observer in self.observers:
            observer()

    @property
    def temperature(self):
        return self._temperature


    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self._update_observers()

class ComputerObserver(object):

    def __init__(self, car_computer):
        self.car_computer  = car_computer

    def __call__(self, *args, **kwargs):
        print(self.car_computer.temperature)

if __name__ == '__main__':
    comp1 = CarComputer(10)
    obs1 = ComputerObserver(comp1)
    comp1.add_observer(obs1)
    comp1.temperature = 20