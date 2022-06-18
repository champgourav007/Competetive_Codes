a, b = [int(i) for i in input().split()]
column = [0] + [int(i) for i in input().split()]
coff = [-1] + [-1 for i in range(a)]
pro = set()
lis = []
for i in range(b):
    id, m,n,o,p = input().split(",")
    id = int(id[8:])
    m = float(m)
    n = int(n[2:])
    o = int(o[2:])
    p = int(p[2:])
    lis.append([m, id, 1, n])
    lis.append([m, id, 2, o])
    lis.append([m, id, 3, p])
lis.sort(key=lambda x: (-x[0], x[1], x[2]))
# print(*lis,sep="\n")

for i in lis:
    print(i)
    if i[1] not in pro:
        if column[i[3]] > 0:
            column[i[3]] -= 1
            coff[i[3]] = i[0]
            pro.add(i[1])
column = [[column[i], i, coff[i]] for i in range(1, len(column))]
column.sort(key=lambda x:(-x[0], x[1], x[2]))
count = 0
for i in lis:
    if i[1] not in pro:
        while count < len(column) and column[count][0] <= 0:
            count += 1
        if count < len(column):
            column[count][0] -= 1
            if column[count][2] == -1:
                column[count][2] = 100
            column[count][2] = min(column[count][2], i[0])
            pro.add(i[1])
column.sort(key=lambda x:-x[2])

for i in column:
    if i[2] != -1:
        print("C-" + str(i[1]), i[2])
    else:
        print("C-" + str(i[1]), "n/a")