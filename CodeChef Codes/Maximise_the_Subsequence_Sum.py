t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    i = 0
    while k > 0:
        if arr[i] < 0:
            arr[i] = abs(arr[i])
        k-=1
        i+=1
    sum = 0
    # print(arr)
    for i in arr:
        if i < 0:
            continue
        else:
            sum += i
    print(sum)
    t-=1
    