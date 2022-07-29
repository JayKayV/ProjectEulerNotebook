w = set([o for o in range(1, 10)])

def getrow(a, j):
    _w = set()
    for i in range(9):
        if a[j][i] != 0:
            _w.add(a[j][i])
    return _w

def getcolumn(a, j):
    _w = set()
    for i in range(9):
        if a[i][j] != 0:
            _w.add(a[j][i])
    return _w
    
def getregion(a, i, j):
    _w = set()
    u, v = 3 * (i // 3), 3 * (j // 3)
    for _i in range(3):
        for _j in range(3):
            k1, k2 = u + _i, v + _j
            if a[k1][k2] != 0:
                _w.add(a[k1][k2])
    return _w

def deduce(a):
    r = []
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0:
                v = copy(w)
                _a, _b, _c = getrow(a, i), getcolumn(a, j), getregion(a, i, j)
                v -= _a
                v -= _b
                v -= _c
                if len(v) == 1:
    return r
                    
        
m = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
a = list(map(int, [m[i:i+9] for i in range(len(m))]))
print(a)
