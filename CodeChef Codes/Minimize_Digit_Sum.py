def sumOfDigit(n, b):
    unitDigit = 0
    sum = 0
    while (n > 0):
        unitDigit = n % b
        sum += unitDigit
        n = n // b
    return sum


t = int(input())
while t > 0:
    val,n,b = map(int,input().split())
    arr = []
    mini = float("inf")
    pos = 0
    while n != b:
        sum = sumOfDigit(val,n)
        if mini > sum:
            mini = sum
            pos = n
        n+=1
    print(pos)
    t-=1