t = int(input())
while t > 0:
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(k):
        arr[n%i] = arr[i%n] ^ arr[n-(i%n)-1]
        a = arr[i%n]
        b = arr[n-(i%n)-1]
        
    print(*arr)
    t-=1