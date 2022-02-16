t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    if n == 1:
        print("YES")
        continue
    countDict = {0:0,1:0}
    for i in arr:
        if i == '1':
            countDict[1] += 1
        else:
            countDict[0] += 1
    if countDict[1] == 1 and countDict[0] == 1:
        print("YES")
    else:
        print("NO")