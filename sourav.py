from collections import defaultdict
def sol(arr, n):
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    res = 0
    for key,value in d.items():
        if key == value:
            continue
        else:
            if key < value:
                res += (value-key)
            else:
                res += value
    return res
            

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol(arr, n))