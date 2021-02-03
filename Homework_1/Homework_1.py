# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
def task1():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data = {}
    for key in keys:
        data[key] = key * key
    print(data)


# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
def task2():
    arr = list(range(0, 101, 2))
    print(arr)


# 3)Заменить в произвольной строке согласные буквы на гласные. 
def task3():
    letters = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    s = 'Hello Wordl!'
    new_s = ''.join(i if i not in letters else 'A' for i in s)
    print(new_s)


# 4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
def task4():
    arr = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

    # 4.1) убрать из него повторяющиеся элементы
    arr2 = list(set(arr))
    print(arr2)

    # 4.2) вывести 3 наибольших числа из исходного массива
    print(sorted(arr)[-3:])

    # 4.3) вывести индекс минимального элемента массива
    print(arr.index(min(arr)))

    # 4.4) вывести исходный массив в обратном порядке
    print(arr[::-1])


task4()


# 5) Найти общие ключи в двух словарях:
# dict_one = { ‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’: 4 }
# dict_two = { ‘a’: 6, ‘b’: 7, ‘z’: 20, ‘x’: 40 }
def task5():
    dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
    diff = dict_one.keys() & dict_two.keys()
    print(diff)


task5()
# 6)Дан массив из словарей
def task6():
    data = [
        {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
        {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
        {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
        {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
        {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
        {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}
    ]

# 6.1) отсортировать массив из словарей по значению ключа ‘age'
    data.sort(key=lambda key: key['age'])
    print(data)
# 6.2) сгруппировать данные по значению ключа 'city'
# вывод должен быть такого вида :
# result = {
#    'Kiev': [
#       {'name': 'Viktor', 'age': 30 },
#       {'name': 'Andrey', 'age': 34}],
#
#    'Dnepr': [ {'name': 'Maksim', 'age': 20 },
#               {'name': 'Artem', 'age': 50}],
#    'Lviv': [ {'name': 'Vladimir', 'age': 32 },
#              {'name': 'Dmitriy', 'age': 21}]
# }
# =======================================================
    data.sort(key=lambda key: key['city'])
    result = {}
    for item in data:
        key = item.get('city')
        if key not in result.keys():
            result[key] = []
        result[key].append(item)
    print(result)
task6()

# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:
#most_frequent(['a', 'a', 'bi', 'bi', 'bi'])== 'bi'
def most_frequent(list_var):
    data = {}
    for i in list_var:
        if i in data.keys():
            continue
        count = 0
        for j in list_var:
            if i == j:
                count += 1
        data[i] = count
    data = list(data.items())
    data.sort(key=lambda key: key[1], reverse=True)
    return data[0][0]

print(most_frequent(['a', 'a', 'bi', 'bi', 'bi']))
# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

def task8(number):
    number = str(number)
    result = 1
    for digit in number:
        if digit == '0':
            continue
        result *= int(digit)
    return result
print(task8(4529))

# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
def task9(array, n):
    if n > len(array) - 1:
        return -1
    return array[n]**n
print(task9([0,1,2,3,4,5,6,7,8,9], 10))

# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.


def task10(string):
    arr = string.split()
    count = 0
    for i in arr:
        if count == 3:
            return True
        if i.isnumeric():
            count = 0
            continue
        count += 1
    return False
print(task10('hello 1 one three 15 ffff fffff fffff'))