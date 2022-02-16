t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    arr = list(zip(a,b))
    sortedArr = sorted(arr, key= lambda x:x[0])

    for i in range(n):
        if sortedArr[i][0] <= k:
            k += sortedArr[i][1]
        else:
            break
    print(k)