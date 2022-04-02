t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    val = n
    while val >= 4:
        val //= 2
        count+=1

    print(n-count-2)


