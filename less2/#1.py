'''Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса.'''

class Automobile:

    def __init__(self, t, a, c):

        self._top_speed = t
        self._accelerations = a
        self._carrying_capacity = c


class Car(Automobile):

    def __init__(self, g):
        self._carrying_capacity = g

    def set_model(self, m):
        self._model = m


class Truck(Automobile):

    def __init__(self, v):

        self._carrying_capacity = v


