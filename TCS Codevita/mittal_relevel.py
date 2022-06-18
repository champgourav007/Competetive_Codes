n = int(input())
arr = list(map(int, input().split()))
m = 0
for i in range(1,n):
    if arr[i] < arr[i-1]:
        diff = arr[i-1] - arr[i]
        arr[i] += diff
        m = max(diff, m)
i = 1
while m > (2**i)-1:
    i+=1
print(i)
