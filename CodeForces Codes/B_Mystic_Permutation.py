from itertools import permutations

def check(arr, new_arr):
    i = 0
    while i < len(arr):
        if arr[i] == new_arr[i]:
            return False
        i+=1
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        print("-1")
        continue
    new_arr = sorted(arr)
    flag = 0
    if check(arr, new_arr):
        print(*new_arr)
        flag = 1
    else:
        permutation = permutations(new_arr)
        for i in permutation:
            if check(arr, i):
                print(*i)
                flag = 1
                break
    if not flag:
        print("-1")
    
            
