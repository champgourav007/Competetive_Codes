t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    s = input()
    if '0' in s and '1' in s:
        res = y if y <= x else x
        print(res)
    else:
        print(0)