from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if n == 1:
        print("3")
    else:
        d = defaultdict(int)
        for i in l:
            d[i] += 1
        s = 0
        v = 0
        for i in d.values():
            if i%2:
                s+=1
            v += i
        if (s+v)%4 == 0:
            print(s)
        else:
            s += (s+v)%4
            print(s)