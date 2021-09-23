n = int(input())
arr = input().split()
i = 0
sum = 0
while i < n:
    sum += int(arr[i])
    i+=1
div = sum//4
if sum%4 != 0:
    div+=1
print(div)