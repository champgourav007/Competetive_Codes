t = int(input())
for _ in range(t):
    n = int(input())
    if n%2:
        v = (n//2) + 1
        print(f"-{v}")
    else:
        v = (n//2)
        print(v)