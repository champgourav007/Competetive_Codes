t = int(input())
while t > 0:
    n,s = map(int,input().split())
    sumArray = (n*(n+1))//2
    res = sumArray - s
    if res >= 1 and res <= n:
        print(res)
    else:
        print("-1")
    t-=1