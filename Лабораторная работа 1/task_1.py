# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Table:
    def __init__(self, length: Union[int, float], height: Union[int, float], contents: list):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param height: Высота стола
        :param contents: Содержимое стола

        Пример:
        >>> table_1 = Table(700, 600, ["Книга", "Ручка"]) #  инициализация экземпляра класса
        """
        if not isinstance(length, Union[int, float]) or not isinstance(height, Union[int, float]):
            raise TypeError("Некорретный тип размера")
        if not isinstance(contents, list):
            raise TypeError("Некорретный тип содержимого стола")
        if length < 0 or height < 0:
            raise ValueError("Некорректное значение размера")

        self.length = length
        self.height = height
        self.contents = contents

    def put_on(self, item: str):
        """
        Функция, которая позволяет положить предмет на стол

        :param item: Предмет, который кладем на стол

        Пример:
        >>> table_1 = Table(700, 600, ["Книга", "Ручка"]) #  инициализация экземпляра класса
        >>> table_1.put_on("Карандаш")
        """
        if not isinstance(item, str):
            raise TypeError("Некорретный тип предмета")
        ...

    def put_off(self, item: str):
        """
        Функция, которая позволяет взять предмет со стола

        :param item: Предмет, который мы забираем со стола

        Пример:
        >>> table_1 = Table(700, 600, ["Книга", "Ручка"]) #  инициализация экземпляра класса
        >>> table_1.put_off("Ручка")
        """
        if not isinstance(item, str):
            raise TypeError("Некорретный тип предмета")
        ...


class Dog:
    def __init__(self, weight: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Собака"

        :param weight: Вес собаки
        :param color: Окрас собаки

        Пример:
        >>> dog_1 = Dog(30, "Белая")    #   инициализация экземпляра класса
        """
        if not isinstance(weight, Union[int, float]) or not isinstance(color, str):
            raise TypeError("Некорректный тип данных")
        if weight < 0:
            raise ValueError("Некорректный вес")

        self.weight = weight
        self.color = color

    def bark(self):
        """
        Функция, которая проверяет, лает ли собака на чужих людей

        :return: Возвращает ответ "Да" или "Нет"

        Пример:
        >>> dog_1 = Dog(30, "Белая")     # инициализация экземпляр класса
        >>> dog_1.bark()
        """
        ...

    def walk(self):
        """
        Функция, которая проверяет, выгуляли ли собаку

        :return: Возвращает ответ "Да" или "Нет"

        Пример:
        >>> dog_1 = Dog(30, "Белая")     # инициализация экземпляр класса
        >>> dog_1.walk()
        """
        ...

    def lying(self):
        """
        Функция, которая проверяет, лежит ли собака на диване

        :return: Возвращает ответ "Да" или "Нет"

        Пример:
        >>> dog_1 = Dog(30, "Белая")     # инициализация экземпляр класса
        >>> dog_1.lying()
        """
        ...


class Pen:
    def __init__(self, color: str, is_writing: bool, type_of_pen: str):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param color: Цвет ручки
        :param is_writing: Пишет ручка или нет
        :param type_of_pen: Тип ручки

        Пример:
        >>> pen_1 = Pen("Черная", True, "Шариковая")    #   инициализация экземпляра класса
        """
        if not isinstance(color, str) or not isinstance(is_writing, bool) or not isinstance(type_of_pen, str):
            raise TypeError("Некорректный тип данных")

        self.color = color
        self.is_writing = is_writing
        self.type_of_pen = type_of_pen

    def write(self):
        """
        Функция, которая проверяет, пишет ли ручка

        :return: Возвращает ответ "Да" или "Нет"

        Пример:
        >>> pen_1 = Pen("Черная", True, "Шариковая")    #   инициализация экземпляра класса
        >>> pen_1.write()
        """
        ...

    def out_of_ink(self):
        """
        Функция, которая проверяет, есть ли чернила в ручке

        :return: Возвращает ответ "Да" или "Нет"

        Пример:
        >>> pen_1 = Pen("Черная", True, "Шариковая")    #   инициализация экземпляра класса
        >>> pen_1.out_of_ink()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()       # тестирование примеров, которые находятся в документации
 