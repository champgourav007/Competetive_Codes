t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    i = 0
    while i < min(a, b):
        print("01", end="")
        i+=1
    for i in range(abs(a-b)):
        if a < b:
            print("1", end="")
        else:
            print("0", end="")
    print()   