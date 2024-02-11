from collections import defaultdict
def sol(arr, n):
    s = []
    dict = defaultdict(list)
    s.append(arr[0])
    for i in range(1, n):
        if len(s) == 0:
            s.append(arr[i])
            continue
        
        while len(s) != 0 and s[-1] > arr[i]:
            dict[s[-1]].append(arr[i])
            s.pop()
        s.append(arr[i])
        
    while len(s) != 0:
        dict[s[-1]].append(-1)
        s.pop()
        
    res = []
    for i in range(n):
        res.append(dict[arr[i]].pop(0))
    return res

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol(arr, n))