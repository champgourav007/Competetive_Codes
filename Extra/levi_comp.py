def sol(n, arr):
    s = []
    for i in range(n):
        s.append([i+1, arr[i]])
    s.sort(reverse=True, key = lambda x:x[1])
    res = []
    res.append([s[0][1],s[0][0]])
    f = []
    f.append(s[0][0])
    for i in range(1,n-1):
        if s[i][1] + s[i+1][1] >= res[-1][0]:
            res.append([s[i][1],s[i][0]])
            f.append(s[i][0])
    if s[-1][1] == res[-1][0]:
        f.append(s[-1][0])
    
    return [len(f), sorted(f)]

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        s = int(input())
        arr.append(s)
    count, res = sol(n, arr)
    print(count)
    print(*res)