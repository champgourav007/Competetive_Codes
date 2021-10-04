size = int(input())
arr = input()
i = 1
count = 0
while i < size:
    j = i-1
    if arr[i] == arr[j]:
        count+=1
    i+=1
print(count)