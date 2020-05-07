'''Создать класс автомобиля. Описать общие аттрибуты. Создать
классы легкового автомобиля и грузового. Описать в основном
классе базовые аттрибуты для автомобилей. Будет плюсом если в
классах наследниках переопределите методы базового класса.'''


class Automobile:

    def __init__(self ,t ,a ,c):
        self._name = a
        self._top_speed = t
        self._carrying_capacity = c

    def get_name(self):
        return self._name

    def set_name(self, m):
        self._name = m

    def get_top_speed(self):
        return self._top_speed

    def set_top_speed(self ,m):
        self._top_speed = m

    def get_carrying_capacity(self):
        return self._carrying_capacity

    def set_carrying_capacity(self ,m):
        self._carrying_capacity = m


class Car(Automobile):

    def __init__(self, c):
        self._carrying_capacity = c


class Truck(Automobile):

    def __init__(self ,c):
        self._carrying_capacity = c



Audi = Automobile('Audi', '100', '2')
print(Audi)

