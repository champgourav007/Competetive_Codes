n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(n):
    j = i+1
    flag = 0
    while j < n:
        if arr[i] <= arr[j]:
            flag = 1
            res.append(j+1)
            break
        j+=1
    if flag == 0:
        res.append(-1)
print(*res)