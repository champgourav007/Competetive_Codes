t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    even, odd = 0, 0
    for i in arr:
        if i%2:
            odd += 1
        else:
            even += 1
    if odd == 0 or even == 0:
        print(0)
        continue
    if even < odd:
        res = even
    elif even > odd:
        if odd%2==0:
            res = odd//2
        else:
            res = odd//2
    else:
        res = even//2 + even%2
    print(res)