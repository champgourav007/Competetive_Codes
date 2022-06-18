n,q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
s = [0 for i in range(n+1)]
for i in range(n):
    s[i+1] = s[i] + arr[i]
print(s) 

for _ in range(q):
    x,y = map(int, input().split())
    if x == y:
        x+=1
    temp = sum(arr[:x][::-1][:y])
    # s, i = 0, 0
    # for i in range(y):
    #     s += temp[i]
    #     i+=1
    print(temp)