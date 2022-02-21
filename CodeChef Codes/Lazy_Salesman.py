t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr) <= w:
        print("0")
    else:
        arr.sort(reverse=True)
        count = 0
        for i in range(n):
            w-= arr[i]
            if w <= 0:
                break
            else:
                count+=1
        print(n-count-1)