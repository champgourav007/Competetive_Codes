t = int(input())

while t > 0:
    arr = list(map(int,input().split()))
    count0 = arr.count(0)
    count1 = arr.count(1)
    if count0 > count1:
        print("NO")
    else:
        print("YES")
    t-=1