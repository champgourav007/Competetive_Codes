def sol(n, arr):
    count = 0
    prev = arr[0]
    flag = 0
    for i in range(n):
        if arr[i] != prev:
            count += 1
            flag = 1
        prev = arr[i]
    return count + flag

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol(n, arr))