matrix = []
i = 0
while i < 5:
    row = input().split()
    matrix.append(row)
    i+=1
flag = 0
row = 0
for i in matrix:
    col = 0
    for j in i:
        if int(j) == 1:
            flag = 1
            break
        col += 1
    if flag == 1:
        break
    row += 1
    
diff = abs(2-row) + abs(2-col)
print(diff)