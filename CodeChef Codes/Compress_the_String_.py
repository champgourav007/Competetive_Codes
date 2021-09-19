string = input()
i = 0
res = []
while i <= len(string)-1:
    j = i+1
    count = 1
    cord = ""
    while j < len(string):
        if string[i] == string[j]:
            count += 1
        else:
            i = j-1
            break
        j+=1
    cord += "(" + str(count) + ", " + str(string[i]) + ")"
    res.append(cord)
    i+=1
    if i != j:
        break
print(*res)