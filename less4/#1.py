from abc import *
from datetime import date

class Person(metaclass=ABCMeta):

    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        print('(Person: {0})'.format(self.name))

    def __str__(self):
        '''Returns complex number as a string'''
        return '(%s, %s,%s,%s)' % (self.name, self.year, self.month, self.day)

    def __repr__(self):
        return '(%s, %s,%s,%s)' % (self.name, self.year, self.month, self.day)

    @abstractmethod
    def tell(self):
        print(f'Name: {self.name}', end='\n')

    @abstractmethod
    def get_age(self):
        today = date.today()
        age = today.year - self.year
        if today.month < self.month:
            age -= 1
        elif today.month == self.month and today.day < self.day:
            age -= 1
        return age


class Entrant(Person):
    '''Абитуриент'''
    def __init__(self, name, year, month, day, faculty):
        Person.__init__(self, name, year, month, day)
        self.faculty = faculty
        print(f'Entrant: {self.name},  date of birth: {self.day}.{self.month}.{self.day}, faculty: {self.faculty} ',
              end='\n')

    def get_age(self):
        age = super().get_age()
        return age

    def tell(self):
        Person.tell(self)
        print(f'Name: {self.name}', end='\n')


class Student(Person):
    '''Студент'''
    def __init__(self, name, year, month, day, faculty, year_of_study):
        Person.__init__(self, name, year, month, day)
        self.faculty = faculty
        self.year_of_study = year_of_study
        print(f'Student: {self.name},  date of birth: {self.day}.{self.month}.{self.day}, faculty: {self.faculty}, '
              f'year_of_study: {self.year_of_study} ', end='\n')

    def get_age(self):
        age = super().get_age()
        return age

    def tell(self):
        Person.tell(self)
        print(f'Name: {self.name}', end='\n')


class Teacher(Person):
    '''Преподаватель'''
    def __init__(self, name, year, month, day, faculty, position, experience):
        Person.__init__(self, name, year, month, day)
        self.faculty = faculty
        self.position = position
        self.experience = experience
        print(f'Teacher: {self.name},  date of birth: {self.day}.{self.month}.{self.day}, faculty: {self.faculty}, '
              f'position: {self.position}, experience: {self.experience} ', end='\n')

    def get_age(self):
        age = super().get_age()
        return age

    def tell(self):
        Person.tell(self)
        print('Faculty: "{0}"'.format(self.faculty))

t = Teacher('Smith', 1965, 4, 1,'Art','Professor', 20)
s = Student('Johnson', 1999, 1, 12, 'Art', 1)
ent = Entrant('Williams', 2002, 3, 12, 'Art')


def age_returne(list_of_persons):
    min_age = int(input('min age: ').strip())
    list_of_age = list(filter(lambda x: min_age <= x.get_age(), list_of_persons))
    return list_of_age


list_of_persons = [Entrant('Williams', 2005, 3, 12, 'Art'),
                Student('Johnson', 1999, 1, 12, 'Art', 1),
                Teacher('Smith', 1965, 4, 1,'Art','Professor', 20)]

l = []

for p in age_returne(list_of_persons):
    l.append(p)
    print(l)


