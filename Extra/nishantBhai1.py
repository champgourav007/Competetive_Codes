t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    count = 0
    while i <= n-k:
        c = arr[i:i+k].count(1)
        if c == m:
            count += 1
        i += 1
    print(count)
