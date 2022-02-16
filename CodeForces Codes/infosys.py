string = input()
alphCount = {}
for i in string:
    if i not in alphCount:
        alphCount[i] = 1
    else:
        alphCount[i] += 1
maxAlpha, maxNum = 0, 0
for i,j in alphCount.items():
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        if maxAlpha < j:
            maxAlpha = j
    if (i >= '0' and i <= '9'):
        if maxNum < j:
            maxNum = j
pos = abs(maxAlpha - maxNum)
val = string[pos]
res = ""
for i in string:
    if i == val and val != " ":
        continue
    elif i == " ":
        res += "$"
    else:
        res += i
print(res)