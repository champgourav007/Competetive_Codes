n,k = map(int, input().split())
arr = list(map(int, input().split()))
a = arr[:]
arr.sort()
val = list(enumerate(arr))
dic = {i[1]: i[0] for i in val}
flag = 0
for i in a:
    if dic[i] >= k:
        print(i)
        flag = 1
        break
if flag == 0:
    print(arr[n-1])