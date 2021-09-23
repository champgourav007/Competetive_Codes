t = int(input())
x = 0
while t > 0:
    val = input()
    if "+" in val:
        x+=1
    if "-" in val:
        x-=1
    t-=1
print(x)