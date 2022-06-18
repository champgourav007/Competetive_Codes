from collections import defaultdict
def print1(pos,d, n, seats):
    result = []
    row = ""
    for i in range(len(d)):
        for j in range(d[i][1]):
            row += str(d[i][0]) + "X"
    row = row[:-1]

    if seats[pos][1] != 0:
        s=""
        s += str("X_"*seats[pos][1])
        row += s

    result.append(row)
    return result


def print2(pos,d, n, seats):
    result = []
    row = ""
    for i in range(len(d)):
        for j in range(d[i][1]):
            row += "X" + str(d[i][0])
    row += "X"
    if seats[pos][1] != 0:
        s=""
        s += str("X_"*seats[pos][1])
        row += s

    result.append(row)
    return result


def sol(p, seats, n):
    res = defaultdict(list)
    for priority,g in p:
        for row in range(n):
            if seats[row][1] >= g:
                res[row].append([priority,g])
                seats[row][1] -= g
                break
    pos = 0
    count = 0
    for i in seats:
        if i[0][0] == "_":
            if res.get(pos):
                result = print1(pos,res[pos], n, seats)
                print(*result)
            else:
                print(seats[pos][0])
        else:
            if res.get(pos):
                result = print2(pos,res[pos], n, seats)
                print(*result)
            else:
                print(seats[pos][0])
        count += 1
        pos+=1
    # print(count)



n = int(input())
seats = []
for i in range(n):
    row = input().strip()
    vacant = row.count("_")
    seats.append([row, vacant])
g = list(map(int, input().split(",")))
count = len(g)
mid = count//2

p = []
i = mid
priority = 1
while i < count:
    p.append([priority, g[i]])
    i+=1
    priority+=1
j = mid-1
while j >= 0:
    p.append([priority, g[j]])
    priority+=1
    j-=1
p.sort(key=lambda x:x[0])
sol(p, seats, n)

