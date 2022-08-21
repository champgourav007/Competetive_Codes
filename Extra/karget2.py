import math

def sol(n, c):
    if n == 1:
        return 3
    if n == 2:
        return 2
    distance = set()
    for i in range(n-1):
        x1, y1 = c[i]
        for j in range(i+1, n):
            x2, y2 = c[j]
            d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            distance.add(d)
    if len(distance) == 1:
        return 3
    else:
        return 4 - (len(distance)-1)

if __name__ == "__main__":
    n = int(input())
    c = []
    for i in range(n):
        values = list(map(int, input().split()))
        c.append(values)
    print(sol(n, c))