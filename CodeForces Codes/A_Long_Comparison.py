def power(x,p):
    if p == 0:
        return 1
    temp = power(x,p//2)
    if p%2 == 0:
        return temp*temp
    else:
        return temp*temp*x

t = int(input())
for _ in range(t):
    x1,p1 = map(int, input().split())
    x2,p2 = map(int, input().split())
    val1 = x1 * power(10,p1)
    val2 = x2 * power(10,p2)
    if val1 > val2:
        print(">")
    elif val1 < val2:
        print("<")
    else:
        print("=")