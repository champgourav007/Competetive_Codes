import math
t = int(input())
for _ in range(t):
    n = int(input())
    res_a = 0
    res_b = 0
    lcm = float("inf")
    for i in range(1,n+1):
        if n%i == 0 and  i*(n//i) == n:
            val = i*(n//i)//math.gcd(i,n//i)
            if lcm > val:
                lcm = val
                res_a = max(i, n//i)
                res_b = min(i, n//i)
    print(res_a, res_b)
