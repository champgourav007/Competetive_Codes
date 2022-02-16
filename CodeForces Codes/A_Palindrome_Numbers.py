num = input()
i = 0
j = len(num)-1
flag1 = 0
flag = 0
while i <= j:
    if num[i] == num[j]:
        i+=1
        j-=1
        flag = 2
    elif flag == 0 and num[j] == '0':
        j-=1
    else:
        print("NO")
        flag1 = 1
        break
if flag1 == 0:
    print("YES")