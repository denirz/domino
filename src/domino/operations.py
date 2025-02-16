from domino.pieces import Piece
from copy import deepcopy
def createpeice():
    for i in range(1,7):
        for j in range(i,7):
            if i == j: continue
            yield Piece(i,j)

def createset():
    ps = set()
    for p in createpeice():
        ps.add(p)
    return ps


def sum5(p1:Piece,p2:Piece,p3:Piece,p4:Piece,p5:Piece):
    res = p1.a/p1.b + p2.a/p2.b + p3.a/p3.b + p4.a/p4.b+ p5.a/p5.b
    return res

def sum5options(p1:Piece,p2:Piece,p3:Piece,p4:Piece,p5:Piece):
    for p1  in [p1,p1.flip()]:
        for p2 in [p2,p2.flip()]:
            for p3 in [p3,p3.flip()]:
                for p4 in [p4,p4.flip()]:
                    for p5 in [p5,p5.flip()]:
                        d = sum5(p1,p2,p3,p4,p5)
                        # print(f"d={d}: {p1} {p2} {p3} {p4}")
                        if d >= 9.99 and d <= 10.01:
                            return p1,p2,p3,p4,p5
                            print(f"founded: {p1} + {p2} + {p3} + {p4} = {d}")
                        pass
                pass
            pass
        pass
    return None

from itertools import permutations
def select5items(d):
    # d=createset()
    s = permutations(d,5)
    for i in s:
        # print(i)
        if sum5options(*i):
            # print(f"found: {i},sum={sum5(*i)}")
            yield i

def splitpool(setitems,d):
    # print(setitems)
    # print(f"{len(d)}:d={d}")

    for i in setitems:
        assert  i in d, f" {i}not  in {d}"
        d.remove(i)
    return setitems

def searchsolution(d):
    N=0
    if len(d)==0: return "set is empty"
    for set1 in select5items(d):
        # print(f"set1 ={set1}")
        fset1 = splitpool(set1,d)
        # print(f" осталоаьс1 {len(d)}")
        # print(f"Fset1 ={fset1}")
        for set2 in select5items(d):
            fset2 = splitpool(set2, d)
            # print(f"set2 = {set2}")
            # print(f" осталоаьс2 {len(d)}")

            assert len(d) == 5
            set3 = sum5options(*d)
            # print(f"set3 = {set3}")
            if set3 == None:
                for s in set2:
                    d.add(s)
                continue
            else:
                N=N+1
                print(f"====={N}=====")
                print(set1)
                print(set2)
                print(set3)
                for s in set3:
                    d.add(s)
                for s in set2:
                    d.add(s)
                continue

        for s in set1:
            d.add(s)

