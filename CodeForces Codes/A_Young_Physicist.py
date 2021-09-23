t = int(input())
lst = []
while t > 0:
    x = list(map(int,input().split()))
    lst.append(x)
    t-=1
sumX = 0
sumY = 0
sumZ = 0
for i in lst:
    sumX += i[0]
    sumY += i[1]
    sumZ += i[2]

if sumX == 0 and sumY == 0 and sumZ == 0:
    print("YES")
else:
    print("NO")