t = int(input())
for _ in range(t):
    num = input()
    n = len(num)
    temp = int(num)
    i = n-1
    power = n-2
    maxVal = 0
    while i > 0:
        temp1 = temp // (10**power)
        val1 = temp1%10
        val2 = temp1//10
        sum = val1+val2
        rem = temp% (10**(power+1))
        res = str(sum)+str(rem)
        maxVal = max(maxVal, int(res))
        i-=1
        print(maxVal,res,sum,rem)