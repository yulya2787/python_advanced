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


class Queue:

    def __init__(self):
        self.people = []

    def add(self, person):
        self.people.insert(0, person)

    def remove(self):
        return self.people.pop()

    def size(self):
        return len(self.people)


s = Stack()
s.push('hello')
s.push('true')
print(s.pop())


class Operation:

    def plus(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)



ob = Operation()
x = complex(5, 6)
y = complex(7, 8)
print(ob.plus(x, y))
print(ob.minus(x, y))
