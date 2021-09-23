str1 = input()
str2 = input()
flag = 0
leng = len(str1)
for i in range(0,leng):
    if str1[i].lower() == str2[i].lower():
        continue
    elif str1[i].lower() < str2[i].lower():
        flag = 1
        break
    else:
        flag = 2
        break
if flag == 0:
    print("0")
elif flag == 1:
    print("-1")
else:
    print("1")
    