t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mini = min(a)
    for i in range(len(a)-1):
        if a[i] == 0:
            continue
        else:
            mini = 0
            for j in range(i+1, n):
                a[j] -= a[i]
            

    if a[n-1] == k:
        print("YES")
    else:
        print("NO")
