test_cases = int(input())
while test_cases > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    bit = [0] * 32
    for i in range(32):
        for j in arr:
            if j & 1<<i:
                bit[i] += 1
    count = 0
    for i in bit:
        while i > 0:
            rem = i%k
            count+=1
            i = i // k
    print(count)
    test_cases -= 1