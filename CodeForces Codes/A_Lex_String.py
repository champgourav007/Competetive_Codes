t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input()
    b = input()
    a = [i for i in a]
    b = [i for i in b]
    c = ""
    a.sort()
    b.sort()
    count_a, count_b = 0, 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j] and count_a < k:
            c += a[i]
            i+=1
            count_a += 1
            count_b = 0
        elif a[i] > b[j] and count_b < k:
            c += b[j]
            j+=1
            count_b += 1
            count_a = 0
        elif a[i] > b[j] and count_b >= k:
            c += a[i]
            i+=1
            count_b = 0
        elif a[i] < b[j] and count_a >= k:
            c += b[j]
            j+=1
            count_a = 0
    print(c)
