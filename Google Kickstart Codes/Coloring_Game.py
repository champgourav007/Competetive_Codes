def sol(n):
    if n == 1:
        return 1
    res = n//2
    res = res//2
    # print(res)
    return res+1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sol(n))