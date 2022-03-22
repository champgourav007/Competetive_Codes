import math as m
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if x == 0 and y == 0:
        print(0)
        
    else:
        a = x*x
        b = y*y
        v = int(m.sqrt(a+b))
        if v*v == a+b:
            print(1)
        else:
            print(2)