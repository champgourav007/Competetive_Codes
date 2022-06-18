n = int(input())
arr = list(map(int, input().split()))
maxi = max(arr)
d = [0 for i in range(maxi+1)]
for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
res_d = [0 for i in range(maxi+1)]

for i in range(1, maxi+1):
    for j in range(i, maxi+1, i):
        if i == j:
            res_d[i] += (d[j]-1)
        else:
            res_d[i] += d[j]
            res_d[j] += d[i]

for i in range(n):
    print(res_d[arr[i]], end=" ")
        