import math

test_cases = int(input())
while test_cases > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    max_ele = arr[0]
    min_ele = arr[0]
    pos_max = 0
    pos_min = 0
    count = 0
    for i in arr:
        if max_ele < i:
            max_ele = i
            pos_max = count
        if min_ele >= i:
            min_ele = i
            pos_min = count
        count += 1
    arr[pos_max] = min_ele
    count = 0
    for i in arr:
        if i == 0:
            continue
        count += math.floor(i/min_ele)
    print(count)
    test_cases -= 1
        
    
    

