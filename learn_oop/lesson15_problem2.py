# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
# оставить только целые числа и сохранить их в атрибут values в виде списка;
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по
# возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
# "Пустой вектор", если наш вектор не хранит в себе значения

class Vector:
    def __init__(self, *args):
        self.values = [x for x in args if isinstance(x, int)]

    def __str__(self):
        if self.values:
            return f'Вектор{(*sorted(self.values),)}'
        else:
            return 'Пустой вектор'


v1 = Vector(4, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"