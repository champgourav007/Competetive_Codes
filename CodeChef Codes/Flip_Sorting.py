t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = [i for i in s]
    res = []
    for i in range(n-1):
        if s[i] == "1":
            for j in range(i+1, n):
                if s[j] == "0":
                    s[j] = "1"
                else:
                    s[j] = "0"
            res.append([i+1, ])