t = int(input())
while t > 0:
    ran = int(input())
    arr = input()
    res = ""
    for i in arr:
        if i == 'U':
            res += "D"
        elif i == 'D':
            res += "U"
        else:
            res += i
    print(res)
    t-=1
            