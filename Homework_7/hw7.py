# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance.email

    def __set__(self, instance, value):
        if '@' in value and '.' in value:
            instance._email = value
            print("ok")
        else:
            raise ValueError("Email not valid")


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

my_class.email = "novalidemail"
# Raised Exception


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _class = None

    def __call__(cls, *args, **kwargs):
        if not cls._class:
            cls._class = super(Singleton, cls).__call__(*args, **kwargs)
            print("Create new class")
        return cls._class


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
print(c == b)
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IntegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IntegerField:
    pass


class Data:
    number = IntegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number


# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# количество на складе(quantity), доступность(availability), цена(price).
# 2) Добавить товар на склад
# 3) Удалить товар со склада
# 4) Распечатать остаток товара по его имени
# 5) Распечатать остаток всех товаров
# 6) Товар может принадлежать к категории
# 7) Распечатать список товаров с заданной категорией
# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.


# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС

# class Product:
#     def __init__(self, name, details, quantity, availability, price):
#         self.name = name
#         self.details = details
#         self.quantity = quantity
#         self.availability = availability
#         self.price = price
#         Storage.add_product(self)
#
#     def __str__(self):
#         return self.name
#
#
# class Storage:
#     _products = []
#
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def products(self):
#         return self._products
#
#     @staticmethod
#     def add_product(product):
#         Storage._products.append(product)
#
#
# storage = Storage("myStorage")
# p1 = Product("name", "details", 10, True, 100)
#
# print(storage.products[0].quantity)
