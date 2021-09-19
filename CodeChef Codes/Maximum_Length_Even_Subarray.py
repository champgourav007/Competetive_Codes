t = int(input())
while t > 0:
    n = int(input())
    sum = (n*(n+1))//2
    # print(sum)
    if sum%2 == 0:
        # print(sum)
        print(n)
    else:
        n-=1
        print(n)
    t-=1