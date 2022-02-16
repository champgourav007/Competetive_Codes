t = int(input())
for _ in range(t):
    n = int(input())
    res = ""
    val = 97
    for i in range(n):
        if val >= 123:
            val = 97
        res += str(chr(val))
        val+=1
    print(res)