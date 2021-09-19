t = int(input())
while t > 0:
    n = int(input())
    arr = map(int,input().split())
    countEven = 0
    countOdd = 0
    for i in arr:
        if i % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    if n % 2 == 0:
        totEven,totOdd = n//2,n//2
    else:
        totEven = n//2
        totOdd = n//2 + 1
    res = 0
    res += min(totOdd , countEven)
    res += min(totEven , countOdd)
    print(res)
    t-=1