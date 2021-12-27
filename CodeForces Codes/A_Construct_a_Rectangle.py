t = int(input())
for _ in range(t):
    l1,l2,l3 = map(int,input().split())
    if l1+l2 == l3:
        print("YES")
    elif l2+l3 == l1:
        print("YES")
    elif l1+l3 == l2:
        print("YES")
    else:
        if l1 == l2 and l3%2 == 0:
            print("YES")
        elif l1 == l3 and l2%2 == 0:
            print("YES")
        elif l2 == l3 and l1%2 == 0:
            print("YES")
        else:
            print("NO")
    
            