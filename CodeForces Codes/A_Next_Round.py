n,k = map(int,input().split())
arr = list(map(int,input().split()))
val = arr[k-1]
i = 0
count = 0
while i < len(arr) and arr[i] >= val:
    if arr[i] > 0:
        count += 1
    i+=1
print(count)

