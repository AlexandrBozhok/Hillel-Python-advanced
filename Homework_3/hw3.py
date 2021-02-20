# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
import functools


def check_division_remainder(func):
    @functools.wraps(func)
    def wrapper(number):
        remainder = 100 % func(number)
        if remainder == 0:
            print("We are OK!")
        else:
            print(f"Bad news guys, we got {remainder}")
    return wrapper

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))


def check_args_type(func):
    @functools.wraps(func)
    def wrapper(arg):
        if type(arg) == int:
            print(func(arg))
        elif type(arg) == str:
            raise ValueError("string type is not supported")
    return wrapper

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.


def cached(func):
    cache = {}
    cache_calls_counter = 0
    func_call_counter = 0
    @functools.wraps(func)
    def wrapper(number):
        if number in cache.keys():
            nonlocal cache_calls_counter
            cache_calls_counter += 1
            print(f"Used cache with counter = {cache_calls_counter}")
        else:
            nonlocal func_call_counter
            func_call_counter += 1
            result = func(number)
            cache[number] = result
            print(f"Function executed with counter = {func_call_counter}, function result = {result}")
    return wrapper


@cached
@check_args_type
@check_division_remainder
def degree(arg):
    return arg**2


@cached
def summmm(arg):
    return arg + arg


degree(2)
degree(4)
degree(2)
degree(2)
degree(2)
degree(3)
summmm(10)
summmm(10)



