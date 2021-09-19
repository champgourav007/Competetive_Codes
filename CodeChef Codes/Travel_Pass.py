t = int(input())
while t > 0:
    n,a,b = map(int,input().split())
    arr = input()
    count0 = arr.count("0")
    count1 = arr.count("1")
    totMin = (count0 * a) + (count1 * b)
    print(totMin)
    t-=1
    