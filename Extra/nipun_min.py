from collections import defaultdict
def sol(n, arr):
    temp = sorted(arr)
    pen = 0
    for i in range(1, n):
        pen += abs(temp[i-1] - temp[i])
    return pen

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol(n, arr))