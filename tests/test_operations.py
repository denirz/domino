from domino import operations

def test_createpiece():
    for n,r in  enumerate(operations.createpeice()):
        print(r)
    assert n == 14 # должно получиться 15 элементов


def test_createset():
    d = operations.createset()
    print(d)
    assert len(d) == 15
    print(list(d)[1])


def test_sum4():
    d = operations.createset()
    m=[]
    for i in range(5):
        m.append(d.pop())
    s = operations.sum5(*m)
    print(m)
    print(s)
    m = []
    for i in range(5):
        m.append(d.pop().flip())
    s = operations.sum5(*m)
    print(m)
    print(s)

def test_sum5options():
    d=operations.createset()
    m=[]
    for i in range(5):
        m.append(d.pop())
    res = operations.sum5options(*m)
    print(f"res={res}")

def  test_select_5_items(capsys):
    with capsys.disabled():
        d=operations.createset()
        for n,i in enumerate(operations.select5items(d)):
            assert len(i) == 5
            pass
        print(n)

def test_split(capsys):
    with capsys.disabled():
        d=operations.createset()
        dfixed=operations.createset()
        for n, set5  in enumerate(operations.select5items(dfixed)):
            s = operations.splitpool(set5,d)
            print(f"{s},{operations.sum5(*s)}")
            print(d)
            assert len(d) ==  len(d)
            d=operations.createset()


def test_searchsolution(capsys):
    with capsys.disabled():
        d = operations.createset()
        operations.searchsolution(d)
