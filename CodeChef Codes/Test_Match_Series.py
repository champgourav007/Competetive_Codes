t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    count0 = arr.count(0)
    count1 = arr.count(1)
    count2 = arr.count(2)
    if count1 > count2:
        print("INDIA")
    elif count2 > count1:
        print("ENGLAND")
    else:
        print("DRAW")