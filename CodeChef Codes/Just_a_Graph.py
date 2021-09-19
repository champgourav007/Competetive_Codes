t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    i = 1
    count = 0
    arr1 = [0] * 100000
    for i in range(n):
        arr1[arr[i] - i - 1]+=1
    # print(arr1)
    if arr1[arr[0] - 1] == n:
        print(n) 
    else:
        print(1)
    t-=1