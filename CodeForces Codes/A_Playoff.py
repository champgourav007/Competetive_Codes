t = int(input())
for _ in range(t):
    n = int(input())
    val = 2**n
    if val // 2 == 1:
        print(1)
    else:
        print(val-1)
