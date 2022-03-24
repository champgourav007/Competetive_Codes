t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxi = max(a)
    mini = min(a)
    pos = []
    flag = 0
    count = 0
    for i in range(n):
        if flag != 1 and a[i] == maxi:
            flag = 1
            pos.append(i+1)
        if flag != 2 and a[i] == mini:
            flag = 2
            pos.append(i+1)
    print(pos[0], pos[1])