'''Создать класс точки, реализовать конструктор который инициализирует 3 координаты (x, y, z).
Реалзиовать методы для получения и изменения каждой из координат. Перегрузить для этого
класса методы сложения, вычитания, деления умножения. Перегрузить один любой унарный метод.
Ожидаемый результат: умножаю точку с координатами 1,2,3 на
другую точку с такими же координатами, получаю результат 1, 4, 9.'''

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        return self.x, self.y, self.z

    def get_coord_x(self):
        return self.x

    def get_coord_y(self):
        return self.y

    def get_coord_z(self):
        return self.z

    def set_coord_x(self, x):
        self.x = x

    def set_coord_y(self, y):
        self.y = y

    def set_coord_z(self, z):
        self.z = z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z

    def __floordiv__(self, other):
        return self.x // other.x, self.y // other.y, self.z // other.z

    def __neg__(self):
        return -self.x, -self.y, -self.z

p1 = Point(1, 2, 3)
p2 = Point(2, 3, 4)
print(p2.x)

print(p1.show())
print(p2.show())
print(p1.__add__(p2))
print(p2.__neg__())
"""Phone.description = 'New description'
phone = Phone('Nokia', '12312')
phone.call()

phone2 = MobilePhone('Samsung', 'eqewqeqweqw')
phone2.call()


phone2.description = 'Samsung phone'
print(phone2.description)
print(phone.description)"""


