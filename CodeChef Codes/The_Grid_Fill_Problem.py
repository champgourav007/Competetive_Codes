t = int(input())
while t > 0:
    n = int(input())
    if n%2 == 0:
        i = n
        j = n
        while i >= 1:
            arr = []
            j = n
            while j >= 1:
                arr.append(-1)
                j-=1
            print(*arr)
            i-=1
    else:
        i = n
        j = n
        while i >= 1:
            arr = []
            j = n
            while j >= 1:
                if i == j:
                    arr.append(-1)
                else:
                    arr.append(1)
                j-=1
            print(*arr)
            i-=1
            # print("\n")
    t-=1

