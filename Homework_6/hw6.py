# Задача-1
# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять Если флаг об исключении отсутствует, исключение должно быть поднято.
#
# Задача -2
# Описать задачу выше но уже с использованием @contextmanager
#
# Задача -3
# Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

import os, time
from contextlib import ContextDecorator


class changeDir(ContextDecorator):
    def __init__(self, new_path, exception=None):
        self._old_path = os.getcwd()
        self.new_path = new_path
        self.exception = exception

    def __enter__(self):
        try:
            os.chdir(self.new_path)
        except self.exception:
            print(f"Have error{self.exception}")
            print(os.getcwd())

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._old_path)
        print("exit")
        print(os.getcwd())


def my_func_for_task1():
    with changeDir("../Homework_10", FileNotFoundError):
        print("in contextmanager")


@changeDir("../Homework_10", FileNotFoundError)
def my_func_for_task2():
    print("in function")


class funcExecutionTime(ContextDecorator):
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        self.t = time.time()
        self.func()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.t)


def my_func_for_task3():
    print("Hello World!")
    time.sleep(1)


with funcExecutionTime(my_func_for_task3):
    print("in contextmanager")
