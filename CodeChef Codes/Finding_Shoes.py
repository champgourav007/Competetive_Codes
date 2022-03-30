t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if m >= n:
        print(n)
    else:
        print((n-m)+n)