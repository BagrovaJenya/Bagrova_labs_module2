class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self._pages = pages
        super().__init__(name, author)

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Неправильный тип данных")
        if new_pages <= 0:
            raise ValueError("Неправильное количество страниц")
        self._pages = new_pages


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self._duration = duration
        super().__init__(name, author)

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Неправильный тип данных")
        if new_duration <= 0:
            raise ValueError("Неправильное длина аудиодорожки")
        self._duration = new_duration
