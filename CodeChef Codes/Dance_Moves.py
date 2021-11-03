t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    count = 0
    while x != y:
        if x < y:
            x+=2
            count+=1
        if x > y:
            x-=1
            count +=1
    print(count)
