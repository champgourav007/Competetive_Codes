n = int(input())
arr = list(map(int,input().split()))
pos_lst = []
i = 0
while i < len(arr)-1:
    j = i
    min = arr[i]
    while j < len(arr):
        if min > arr[j]:
            min = arr[j]
            pos = j
        j+=1
    string = ""
    string += str(i) + " " + str(pos)
    temp = arr[pos]
    arr[pos] = arr[i]
    arr[i] = temp
    print("000",arr[pos])
    pos_lst.append(string)
    i+=1
print(len(pos_lst))
for i in pos_lst:
    print(i)
            