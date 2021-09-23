n,k = map(int,input().split(" "))
arr = input().split()
count0 = arr.count("0")
if count0 == n:
    print(0)  
else:
    count = 0
    finisher = int(arr[k-1])
    for i in arr:
        if int(i) >= finisher:
            count += 1
    print(count)
