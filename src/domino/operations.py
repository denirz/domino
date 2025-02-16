from domino.pieces import Piece
from itertools import permutations
def createpeice():
    """ Итератор - создает последовательно все фишки"""
    for i in range(1,7):
        for j in range(i,7):
            if i == j: continue
            yield Piece(i,j)

def createset():
    """  Создает полный набор всех фишек """
    ps = set()
    for p in createpeice():
        ps.add(p)
    return ps


def sum5(p1:Piece,p2:Piece,p3:Piece,p4:Piece,p5:Piece):
    """Функция суммирует 5 фишек """
    res = p1.a/p1.b + p2.a/p2.b + p3.a/p3.b + p4.a/p4.b+ p5.a/p5.b
    return res

def sum5options(p1:Piece,p2:Piece,p3:Piece,p4:Piece,p5:Piece):
    """
    Выбираем 5 фишек и проверяем  можно ли их пенревернуть так чтобы сумма их равнялась 10
    :param p1:
    :param p2:
    :param p3:
    :param p4:
    :param p5:
    :return:  5 верно  повернутых фишек или Nonе если фишки  не суммируются в 10
    """
    for p1  in [p1,p1.flip()]:
        for p2 in [p2,p2.flip()]:
            for p3 in [p3,p3.flip()]:
                for p4 in [p4,p4.flip()]:
                    for p5 in [p5,p5.flip()]:
                        d = sum5(p1,p2,p3,p4,p5)
                        # print(f"d={d}: {p1} {p2} {p3} {p4}")
                        if d >= 9.99 and d <= 10.01:
                            # todo есть какой-то более красивый способ привести  Float в Int  и проверить что  это 10 , но я его сходу не знаю
                            return p1,p2,p3,p4,p5
                            # print(f"founded: {p1} + {p2} + {p3} + {p4} = {d}")
                        pass
                pass
            pass
        pass
    return None


def select5items(d):
    """
    последовательно  возвращает все выборки по 5 фишек из заданного набора.
    но только при условии,  что они в сумму могут дать 10(!)
    :param d:
    :return: set из 5 фишек
    """
    s = permutations(d,5)
    # todo  кажется что  тут возращаются еще и разнве перестановки а нам они не нужны. навернео есть более удачный вариант  permutation
    # это сильно скорит  работу
    for i in s:
        if sum5options(*i):
            yield i

def splitpool(setitems,d):
    """
    удаляет из набора d items setitems
    :param setitems:
    :param d:
    :return:
    """
    for i in setitems:
        assert  i in d, f" {i} not  in {d}"
        d.remove(i)
    return setitems

def searchsolution(d):
    N=0  # счеитчик решений
    if len(d)==0: return "set is empty"
    for set1 in select5items(d): # Выбираем первые 5  дающих 10  ку  ( первый ряд)
        fset1 = splitpool(set1,d) # удаляем  первый ряд из набора
        # print(f" осталоаьс1 {len(d)}") #todo Conver to logger
        # print(f"Fset1 ={fset1}")
        for set2 in select5items(d):  # из оставшихся выбираем 2 ряд дающий 10
            fset2 = splitpool(set2, d) # Удалвем из набора 2 ряд
            # print(f"set2 = {set2}")
            # print(f" осталоаьс2 {len(d)}")

            assert len(d) == 5  # должно остатться только 5 фишек
            set3 = sum5options(*d)    # проверяем  дают ли оставшиеся 5 фишек 10 ку
            # print(f"set3 = {set3}")
            if set3 == None:   # не дают
                for s in set2: # возвращаем обратно в пул 2 ряд
                    d.add(s)
                continue
            else:
                N=N+1
                print(f"====={N}=====")
                print(set1)
                print(set2)
                print(set3)
                # for s in set3: # кажется 3 ряд возвращать не надо ибо мы его не вынимали
                #     d.add(s)
                for s in set2: #возвращаем обратно в пул 2 ряд
                    d.add(s)
                continue

        for s in set1:#  #возвращаем обратно в пул 1 ряд
            d.add(s)

