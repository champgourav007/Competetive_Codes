t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    score = list(map(int,input().split()))
    if 0 not in score:
        print("100")
    else:
        temp_score = score[:m]
        if 0 in temp_score:
            print("0")
        else:
            print(k)
