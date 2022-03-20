t = int(input())
for k in range(t):
    I = input()
    P = input()
    i = 0
    j = 0
    count = 0
    while i < len(I) and j < len(P):
        if I[i] == P[j]:
            i+=1
            j+=1
        else:
            count+=1
            j+=1
    if len(P)-count > len(I):
        count += (len(P)-count) - len(I)
    if len(I) == len(P)-count:
        print(f"Case #{k+1}: {count}")
    else:
        print(f"Case #{k+1}: IMPOSSIBLE")