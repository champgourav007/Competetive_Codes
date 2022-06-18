def sol(p, seats, n):
    result = []
    col = len(seats[0][0])
    print(col)
    for i,j in seats:
        row = []
        for k in i:
            row.append(k)
        result.append(row)
    # print(result)
    r = [0]*n
    for priority,g in p:
        for row in range(n):
            if r[row] == 0:
                r[row] = 1
                i = 0
                j = 0
                count = 0
                # print(g)
                while count <= g:
                    # print(len(result[i]))
                    if i > col-1:
                        j += 1
                        i = 0
                    print(i)
                    if result[j][i] == "_":
                        result[j][i] = priority
                        count += 1
                    i+=1
                
            if seats[row][1] >= g:
                pass
    print(result)

  



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

