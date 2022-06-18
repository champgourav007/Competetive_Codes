def sol(v, t1, t2, n):
    v.sort()
    a = []
    b = []
    c1 = 0
    c2 = 0
    j = t1*v[n-1]
    k = 0
    a.append(v[n-1])
    c+=1
    for i in range(n-2, -1, -1):
        x = j+(t1*v[i])
        y = k+(t2*v[i])
        if x < y:
            a.append(v[i])
            c1+=1
            y = y-(t2*v[i])
            if x < y:
                j = 0
                k = y-x
            else:
                k = 0
                j = x-y
        else:
            x = x-(t1*v[i])
            b.append(v[i])
            c2+=1
            if x < y:
                j = 0
                k = y-x
            else:
                k = 0
                j = x-y
    for i in range(c1):
        print(a[i],end=" ")
    print()
    for j in range(c2):
        print(b[j], end=" ")   


if __name__ == "__main__":
    t1 = int(input())
    t2 = int(input())
    n = int(input())
    v = list(map(int,input().split()))
