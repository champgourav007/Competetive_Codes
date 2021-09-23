n = int(input())
sol = 0
while n > 0:
    arr = input().split()
    count = arr.count("1")
    if count >= 2:
        sol+=1
    n-=1
print(sol)
