l,b = map(int,input().split())
count = 0
while l <= b:
    l *= 3
    b *= 2
    count+=1
print(count)