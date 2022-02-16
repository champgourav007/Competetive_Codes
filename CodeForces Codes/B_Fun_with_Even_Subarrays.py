t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    j = n-1
    count = 0
    while i <= j:
        if arr[i] != arr[j]:
            count+=1
        i+=1
        j-=1
    print(count)