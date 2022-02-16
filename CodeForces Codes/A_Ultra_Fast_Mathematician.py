val1 = input()
val2 = input()
i = 0
res = ""
while i < len(val1):
    if val1[i] == val2[i]:
        res+= str(0)
    else:
        res += str(1)
    i+=1
print(res)