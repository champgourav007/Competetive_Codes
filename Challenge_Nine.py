t = int(input())
for k in range(t):
    n = input()
    s = sum([int(i) for i in n])
    i = 1
    while True:
        val = i*9
        if val >= s:
            break
        i+=1
    diff = val - s
    i = len(n)-1
    res = ""
    flag = 0
    while i >= 0:
        if int(n[i]) > diff:
            res += n[i]
        else:
            res += str(diff)
            flag = 1
            break
        i-=1
    while i >= 0:
        res += str(n[i])
        i-=1
    if flag == 0:
        res += str(diff)
    r = str(int(res[::-1]))
    if len(n) == len(r):
        r = int(str(r)+str(diff))
    print(f"Case #{k+1}: {int(r)}")

