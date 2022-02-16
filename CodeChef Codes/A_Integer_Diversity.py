import collections
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    countDict = collections.defaultdict(int)
    for i in arr:
        countDict[i] += 1
    count = 0
    for i,j in countDict.items():
        if i == 0:
            count += 1
        else:
            if j == 1:
                count += 1
            else:
                count += j - (j%2)
    print(count)
        