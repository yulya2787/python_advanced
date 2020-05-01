'''Создать класс магазина. Конструктор должен инициализировать
значения: «Название магазина» и «Количество проданных
товаров». Реализовать методы объекта, которые будут увеличивать
кол-во проданных товаров, и реализовать вывод значения
переменной класса, которая будет хранить общее количество
товаров проданных всеми магазинами.'''

class Market:

    total = 0

    def __init__(self, name, quontity_of_goods):
        self._name = name
        self.quontity_of_goods = quontity_of_goods

        Market.total += quontity_of_goods


ATB = Market('ATB', 100)
ATB.quontity_of_goods = 100
Novus = Market('Novus', 150)
Novus.quontity_of_goods = 150


print(Market.total)

print(ATB.quontity_of_goods)
print(Novus.quontity_of_goods)