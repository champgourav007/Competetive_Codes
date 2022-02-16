t = int(input())
for _ in range(t):
    string = input()
    countDict = {}
    count = 0
    for i in string:
        if i not in countDict:
            countDict[i] = 1
        else:
            countDict[i] += 1
            count += 1
    res = ""
    if count == 0:
        print(string)
    else:
        for i,j in countDict.items():
            if j == 1:
                res += i
            else:
                res += i*j
        print(res)
    