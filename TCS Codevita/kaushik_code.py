class P:
    def _init_(self, x, y):
        self.x = x
        self.y = y

def func(pnt):
    mn = 0
    for i in range(1, len(pnt)):
        if pnt[i].x < pnt[mn].x:
            mn = i 
        elif pnt[i].x == pnt[mn].x:
            if pnt[i].y > pnt[mn].y:
                mn = i
    return mn

def ont(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def ch(pnt, n):
    if n < 3:
        return 
    l = func(pnt)
    h = []
    p = l 
    q = 0 
    while True:
        h.append(p)
        q = (p + 1) % n
        for i in range(n):
            if ont(pnt[p], pnt[i], pnt[q]) == 2:
                q = i 
        p = q
        if p == l:
            break 
    
    ret = []
    for e in h:
        ret.append(pnt[e])
    return ret

def pA(h):
    area = 0.0
    j = len(h) - 1
    for i in range(len(h)):
        area += (h[j].x + h[i].x) * (h[j].y - h[i].y)
        j = i
    return int(abs(area / 2.0))


if __name__ == "__main__":
    pnt = []
    num = int(input())
    for i in range(num):
        x, y = map(int, input().split())
        pnt.append(P(x, y))
    h = ch(pnt, num)
    print(pA(h))