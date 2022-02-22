t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    j = 1
    for i in arr:
        k = i
        while k >= j:
            res.append(k)
            k-=1
        j = i+1
    print(*res)