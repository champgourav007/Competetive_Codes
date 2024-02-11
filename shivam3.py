def sol(n, arr):
    res = 0
    for i in range(n-1):
        sum = arr[i]
        for j in range(i+1, n):
            sum += arr[i] if arr[i] <= arr[j] else 0
        res = max(res, sum)
    return res
        

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol(n,arr))