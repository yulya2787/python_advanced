class Stack:

    def __init__(self):
        self.items = [ ]

    def isEmpty(self):
        return self.items == [ ]

    def push(self ,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
s.push('true')
print(s.pop())

class Queue:

    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.insert(0, person)

    def remove(self):
        return self.people.pop()

    def size(self):
        return len(self.people)


q = Queue()
q.add('true')
print(q.size())


class Complex(object):

    def __init__(self, a, b):
        '''Creates Complex Number'''
        self.a = a
        self.b = b

    def __str__(self):
        '''Returns complex number as a string'''
        return '(%s, %s)' % (self.a, self.b)

    def __add__(self, other):
        return Complex(self.a + other.a ,
                       self.b + other.b)

    def __sub__(self ,other):
        return Complex(self.a - other.a ,
                       self.b - other.b)


c1 = Complex(0, 1)
c2 = Complex(0, 8)
print(c1.__add__(c2))
print(c2.__sub__(c1))
