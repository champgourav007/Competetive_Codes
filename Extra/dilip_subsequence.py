def sol(n):
    if n == 1:
        return 4
    elif n >= 2 and n <= 4:
        return 5
    else:
        return 0


if __name__ == "__main__":
    n = int(input())
    print(sol(n))