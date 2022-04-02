t = int(input())
for _ in range(t):
    num = int(input())
    s = [int(i) for i in str(num)]
    s = sum(s)
    if s%2:
        s = [int(i) for i in str(num+1)]
        s = sum(s)
        if s%2 == 0:
            print(num+1)
        else:
            print(num+2)
    else:
        s = [int(i) for i in str(num+1)]
        s = sum(s)
        if s%2 == 1:
            print(num+1)
        else:
            print(num+2)