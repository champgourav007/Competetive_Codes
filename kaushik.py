def sol(arr, m):
    s = sum(arr)
    left = 0
    ts = 0
    maxS = -float("inf")
    for i in range(len(arr)):
        ts += arr[i]
        if (i-left)+1 == m:
            maxS = max(maxS,ts)
            ts -= arr[left]
            left += 1
    return s - maxS

if __name__ == "__main__":
    m,n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sol(arr,m))