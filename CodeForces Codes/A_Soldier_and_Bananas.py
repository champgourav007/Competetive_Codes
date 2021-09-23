k,n,w = map(int,input().split())
i = 1
cost = 0 
while w > 0:
    cost += (i*k)
    w -= 1
    i += 1
if cost > n:
    print(cost-n)
else:
    print("0")