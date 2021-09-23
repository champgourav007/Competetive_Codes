t = int(input())
while t > 0:
    k = int(input())
    i = 1
    while k >= 1:
        if i%3 == 0 or i%10 == 3:
            i+=1
            continue
        else:
            i+=1
        k-=1
    print(i-1)
    t-=1