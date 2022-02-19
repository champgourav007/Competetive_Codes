if __name__ == "__main__":
    t = int(input())
    for j in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        h_index = 0
        c = [0]*(n+1)
        res = []
        for i in arr:
            if i > h_index:
                if i <= n:
                    c[i] += 1
                else:
                    c[n] += 1
                if count == c[h_index]:
                    h_index+=1
                    count = 0
                else:
                    count += 1
            res.append(h_index)
        
        print("Case #"+str(j+1)+":", *res)
        