def sol(Arr, k):
    res = 0
    count = 1
    while k:
        c = 0
        for i in Arr:
            if count%i != 0:
                c += 1
        if c == len(Arr):
            res += count
            k-=1
        count += 1
    
    return res
    

if __name__ == "__main__":
    k, n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sol(arr, k))
    