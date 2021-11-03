t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    n+=1
    tot_carry = n*y
    if tot_carry >= x:
        print("YES")
    else:
        print("NO")