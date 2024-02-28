if __name__ == "__main__":
    class Furniture:
        """Базовый класс мебель."""

        def __init__(self, material: str, length: float, height: float, width: float):
            self.material = material
            self._length = length
            self._height = height
            self._width = width

        #    некоторые атрибуты являются защищенными, чтобы пользователь не указал некорректные значения

        def __str__(self) -> str:
            return f"Материал {self.material}, длина {self._length}, высота {self._height}, ширина {self._width}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(material={self.material!r}, length={self._length}, height={self._height}, width={self._width})"

        """Метод размещения предмета на полку"""

        @staticmethod
        def put(item: str) -> str:
            return f"{item} положен на полку"

        """Метод разборки мебели"""

        @staticmethod
        def disassemble() -> str:
            return f"Мебель разобрана"

        """Метод нахождения горизонтальной площади"""

        def area(self) -> float:
            return self._length * self._width


    class Table(Furniture):
        """Дочерний класс стол"""

        def __init__(self, material: str, length: float, height: float, width: float, leg_count: int):
            super().__init__(material, length, height, width)
            self._leg_count = leg_count

        #    атрибут является защищенным, чтобы пользователь не указал некорректное значение

        def __str__(self) -> str:
            return f"Материал {self.material}, длина {self._length}, высота {self._height}, ширина {self._width}, количество ножек {self._leg_count}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(material={self.material!r}, length={self._length}, height={self._height}, width={self._width}, leg_count={self._leg_count})"

        """Перегрузка метода для размещения предмета на стол"""

        @staticmethod
        def put(item: str) -> str:
            return f"{item} положен на стол"
    pass
