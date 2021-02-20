import os
# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)


class IP:
    _ip_list = ["24.15.1.154", "185.195.162.217", "142.11.16.116", "208.76.110.108", "76.93.103.110"]

    @property
    def ip_list(self):
        return IP._ip_list

    @property
    def reverse_ip(self):
        return ['.'.join(ip.split(".")[::-1]) for ip in IP._ip_list]

    @property
    def part_ip(self):
        return ['.'.join(ip.split(".")[1::]) for ip in IP._ip_list]

    @property
    def last_part_ip(self):
        return [ip.split(".")[-1::][0] for ip in IP._ip_list]


ip = IP()
print(ip.ip_list)
print(ip.reverse_ip)
print(ip.part_ip)
print(ip.last_part_ip)


# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу


class File:
    def __init__(self, path: str):
        self.path = path

    def read_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = file.read()
            return data

    def write_data(self, data):
        if os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as file:
                file.write(data)
        else:
            raise FileNotFoundError

    @staticmethod
    def files_data_to_file(filename, *files):
        new_file = File(filename)
        data = ""
        for file in files:
            data += f"{file.read_data()} \n"
        new_file.write_data(data)
        return new_file

    def absolute_path(self):
        return os.path.abspath(self.path)

    def relative_path(self):
        return os.path.relpath(self.path)


f = File("example_json_1.json")
f1 = File("example_json_2.json")
f2 = File.files_data_to_file("new_file.txt", f, f1)
print(f2.absolute_path())
print(f2.relative_path())

# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.


class Connect:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name_value):
        self._unit_name = unit_name_value
        print(f"unit_name changed")

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        self._mac_address = mac_address
        print(f"mac_address changed")

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address
        print(f"ip_address changed")

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login
        print(f"login changed")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
        print(f"password changed")


con = Connect("unit_name", "mac", "ip", "login", "pass")
