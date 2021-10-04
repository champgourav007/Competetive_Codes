num = input()
flag = 1
count = 0
dictLucky = {}
dictLucky[0] = num.count("4")
dictLucky[0] += num.count("7")
val = list(dictLucky.values())
for i in str(val[0]):
    if int(i) == 4 or int(i) == 7:
        continue
    else:
        flag = 0
        break
if flag == 0:
    print("NO")
else:
    print("YES")