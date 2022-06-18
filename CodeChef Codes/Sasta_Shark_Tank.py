t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a*10 > b*5:
        print("FIRST")
    elif a*10 < b*5:
        print("SECOND")
    else:
        print("ANY")