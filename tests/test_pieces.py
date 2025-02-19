import pytest
from domino.pieces import Piece


def test_Piece():
    """
        Тестирует функциональность класса Piece.

        Проверяет следующие случаи:
        - Два объекта Piece с одинаковыми значениями считаются равными.
        - Два объекта Piece с разными значениями считаются неравными.
        - Хеши для одинаковых объектов Piece совпадают.
        - Хеши для разных объектов Piece не совпадают.
        - Метод flip() работает корректно.
        """
    p = Piece(1, 2)
    d = Piece(2, 1)
    e = Piece(1, 3)
    assert p == d
    assert p!=e
    assert p.__hash__() == d.__hash__()
    assert p.__hash__() != e.__hash__()
    print(p)
    p.flip()
    print(p)
    assert p == d