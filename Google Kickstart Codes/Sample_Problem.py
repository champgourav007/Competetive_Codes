if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        s = sum(arr)
        print("Case #"+str(i+1)+": " + str(s%k))
