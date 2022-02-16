n = int(input())
arr = list(map(int, input().split()))
countArr = {1:0,2:0}
for i in arr:
    countArr[i] += 1
count = 0
flag = 0
if countArr[1] == 0:
    count = 0
    flag = 1
if countArr[2] == 0:
    count+= countArr[1]//3
    flag = 1
if flag == 0 and countArr[2] <= countArr[1]:
    count += countArr[2]
    countArr[1] -= countArr[2]
    count += countArr[1] // 3
    flag = 1
if flag == 0 and countArr[2] > countArr[1]:
    count += countArr[1]

print(count)