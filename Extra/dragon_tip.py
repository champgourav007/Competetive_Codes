def sol(n, x, y, a, b):
    i, res = 0, 0
    while x > 0 or y > 0:
        if i >= n:
            break
        if a[i] >= b[i] and x:
            res += a[i]
            x-=1
        elif a[i] < b[i] and y:
            res += b[i]
            y-=1
        i+=1
    return res



if __name__ == "__main__":
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sol(n, x, y, a, b))