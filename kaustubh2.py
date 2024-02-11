def sol(n, m, arr, rep):
    if m == 0:
        return arr
    rep.sort(reverse=True)
    res = []
    j = 0
    for i in arr:
        if j < m and i < rep[j]:
            res.append(rep[j])
            j+=1
        else:
            res.append(i)
    return res
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    rep = list(map(int, input().split()))
    if n == 0:
        print("NULL")
    else:
        print(*sol(n, m, arr, rep))
