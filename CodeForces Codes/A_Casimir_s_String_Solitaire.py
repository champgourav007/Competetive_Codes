t = int(input())
while t:
    s = input()
    countA = s.count("A")
    countB = s.count("B")
    countC = s.count("C")
    if countB == 0:
        print("NO")
    else:
        countB = countB - countA
        if countC == 0 and countB == 0:
            print("YES")
        elif countB > 0 and countB == countC:
            print("YES")
        else:
            print("NO")
    t-=1
    
