n = int(input())
count = n-1
res = ""
for i in range(1,n+1):
    res = ""
    res += " "*count
    res += "* "*i
    count-=1
    print(res)
        