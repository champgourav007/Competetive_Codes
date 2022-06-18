t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    while i < n and m >= arr[i]:
        m -= arr[i]
        i+=1
    if i >= n:
        print("0")
        continue
    else:
        count = 0
        if m != 0:
            count = abs(arr[i]-m)
            i+=1
        count += sum(arr[i:])
        print(count)