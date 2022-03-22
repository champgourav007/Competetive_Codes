t = int(input())
for _ in range(t):
    n,B,x,y = map(int, input().split())
    s = 0
    val1 = 0
    val2 = 0
    # n-=1
    while n:
        val1 += x
        val2 -= y
        if val1 <= B:
            s += val1
            val2 = val1
        elif val2 <= B:
            s += val2
            val1 = val2
        n-=1
    print(s)