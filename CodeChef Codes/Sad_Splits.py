t = int(input())
for _ in range(t):
    n = input()
    countEven = 0
    countOdd = 0
    countZero = 0
    for i in n:
        if i == '0':
            countZero += 1
        if int(i)%2 == 0:
            countEven += 1
        else:
            countOdd += 1
    if countZero != 0:
        if countEven >= 2:
            print("YES")
        else:
            print("NO")
        continue
    if countEven >= 2 or countOdd >= 2:
        print("YES")
    else:
        print("NO")
