
# Вызов декоратора с различными аргументами

# Отлично, с этим разобрались. Что вы теперь скажете о том, чтобы попробовать вызывать декораторы с
# различными аргументами? Это не так просто, как кажется, поскольку декоратор должен принимать функцию в качестве
# аргумента, и мы не можем просто так передать ему что либо ещё. Так что, перед тем, как показать вам решение, я бы
# хотел освежить в памяти то, что мы уже знаем:

# Декораторы - это просто функции
def my_decorator(func):
    print("Я обычная функция")

    def wrapper():
        print("Я - функция, возвращаемая декоратором")
        func()
    return wrapper


# Так что, мы можем вызывать её, не используя "@"-синтаксис:
def lazy_function():
    print("zzzzzzzz")


decorated_function = my_decorator(lazy_function)  # выведет: Я обычная функция


# Данный код выводит "Я обычная функция", потому что это ровно то, что мы сделали:
# вызвали функцию. Ничего сверхъестественного
@my_decorator
def lazy_function():
    print("zzzzzzzz")  # выведет: Я обычная функция

# Как мы видим, это два аналогичных действия. Когда мы пишем @my_decorator — мы просто говорим интерпретатору
# «вызвать функцию, под названием my_decorator». Это важный момент, потому что данное название может как привести
# нас напрямую к декоратору… так и нет!








