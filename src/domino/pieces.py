"""
This module contains the Piece class.
"""


class Piece(object):
    """
    Класс эмулирует фишку домино
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __eq__(self, other):
        """ при переворачивании фишка остается той же самой"""
        if self.a == other.a and self.b == other.b:
            return True
        if self.a == other.b and self.b == other.a:
            return True
        return False

    def __add__(self, other):
        """   может пригодится чтобы складывать фишки"""
        return Piece(self.a * other.b + other.a * self.b, self.b * other.b)

    def __repr__(self):
        """" Отображаем Фишку """
        return f"Piece({self.a}/{self.b})"

    def __hash__(self):
        " И Хэш у фишки остается тем же  при переворачивании"
        return hash(self.a) + hash(self.b)

    def flip(self):
        """ Операция переворачивания фишки"""
        self.a,self.b= self.b,self.a
        return self
