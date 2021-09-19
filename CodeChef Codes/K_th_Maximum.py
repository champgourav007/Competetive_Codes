t = int(input())
while t > 0:
    n,k = map(int,input().split())
    i = 0
    maxi = 0
    arr = list(map(int,input().split()))
    while i < n:
        if maxi <= arr[i]:
            maxi = arr[i]
        i+=1
    count = 0
    k-=1
    for i in range(n):
        x = i+k
        if x < n and arr[x] == maxi:
            count+=(n-x)
    print(count)
    t-=1
    