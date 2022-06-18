t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 2:
        print("YES")
        continue
    count = 0
    maxi = arr[0]
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            if i >= 2 and arr[i-2] > arr[i-1]:
                count += 2
            elif i >= 2 and arr[i-2] < arr[i-1]:
                count += 1
            else:
                count += 1

    if count <= 1:
        print("YES")
    else:
        print("NO")