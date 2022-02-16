#it is not solved till, give time to make it solve
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[0] == arr[n-1]:
        print("0")
        continue
    i = 0
    j = n-1
    # maxi = 0
    # mini = 0
    
    while i < j:
        if arr[i] < arr[j]:
            arr[i] += 1
            arr[j] -= 1
            i+=1
        else:
            j-=1
    print(max(arr)-min(arr))
            