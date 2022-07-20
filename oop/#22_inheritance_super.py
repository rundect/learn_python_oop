"""
Наследование. Функция super() и делегирование
https://proproprogs.ru/python_oop/python-nasledovanie-funkciya-super-i-delegirovanie

-0-
Имеется некий базовый класс Geom и мы создаем дочерний класс Line, в котором прописан метод
draw(), то это называется расширением (extended) базового класса. Как правило, дочерние создаются именно
для расширения функциональности базовых классов
Однако, если в классе Geom также прописать метод draw(), то теперь класс Line лишь переопределяет (overriding)
поведение базового класса, не меняя его принцип функционирования. Поэтому, когда говорят о расширении, то
подразумевают добавление новых атрибутов в дочерних классах, а при переопределении (обычно методов) – изменение
поведения уже существующего функционала.
"""


class Geom:
    name = 'Geom'

    """
    -1-
    Происходит следующая последовательность вызовов магических методов. Сначала вызывается __call__(), который, 
    в свою очередь, последовательно вызывает метод __new__() для создания экземпляра класса, а затем, метод 
    __init__() для его инициализации. Так вот, все эти методы вызываются из дочернего класса Line. Если какой-либо 
    из них не находится, то поиск продолжается в родительских классах в порядке иерархии наследования. Например, 
    метод __new__() в данном случае будет взят из класса object, от которого неявно идет наследование, а вот 
    метод __init__() мы прописали в классе Geom, поэтому будет вызван именно он. Причем, параметр self в этом 
    методе будет ссылаться на созданный объект класса Line. Об этом мы с вами уже говорили и это следует помнить. 
    Параметр self в методах класса всегда ссылается на объект, из которого метод был вызван. 
    """

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = 0


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    """
    -2-
    Для класса Line был вызван инициализатор в базовом классе Geom, а для класса Rect не вызывался – только
    инициализатор самого класса. И это логично, так как метод __init__() был найден в Rect и дальше цепочка
    поиска не продолжалась. Но нам же нужно при создании примитивов также вызывать инициализатор и базового
    класса Geom. Как это сделать? Конечно, мы могли бы явно указать имя базового класса Geom и вызвать через
    него магический метод __init__() в инициализаторе класса Rect. Но явно указывать имена базовых классов не
    лучшая практика, так как имена и иерархия наследования могут меняться. Поэтому в Python для обращения к
    базовому классу используется специальная функция super()
    """
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование прямоугольника")


# l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)

"""
-3-
При запуске программы мы видим, что был вызван инициализатор сначала класса Geom, а затем, для Rect. Такое 
обращение к переопределенным методам базового класса с помощью функции super() называется делегированием. 
То есть, мы делегировали вызов инициализатора класса Geom, чтобы он создал в нашем объекте локальные 
свойства с координатами углов прямоугольника. Причем, вызов метода __init__() базового класса лучше 
делать в первой же строчке, чтобы он случайно не переопределял какие-либо локальные свойство в дочернем классе. 
"""
print(r.__dict__)