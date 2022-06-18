t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    flag = 0
    count0 = s.count('0')
    count1 = s.count('1')
    for i in range(n-1):
        if s[i] == '1' and s[i+1] == '1':
            flag = 1
    if count0 == n:
        print("0")
    elif count1 == n:
        if count1 == 1:
            print("1")
        else:
            print("2")
    else:
        if flag == 1:
            print("2")
        else:
            print("1")
