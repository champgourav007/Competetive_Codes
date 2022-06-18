t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    res = []
    for j in range(2*r + 1):
        k = 2
        row1 = ""
        row2 = ""
        while k <= c:
            if j%2:
                row2 += "|"
                row2 += "."
            else:
                row1 += "+"
                row1 += "-"
            k+=1
        if j%2:
            row2 += "|"

        else:
            row1 += "+"

        if j > 1:
            if j%2:
                row2 +=  "." + "|"
                res.append(row2)
            else:
                row1 += "-" +"+" 
                res.append(row1)
        else:
            if j%2:
                res.append(row2)
            else:
                res.append(row1)

    row1 = res[0]
    row2 = res[1]
    row1 = "." + "." + row1
    row2 = "." + "." + row2
    res[0] = row1
    res[1] = row2 
    print(f"Case #{i+1}:")
    print(*res, sep="\n")
