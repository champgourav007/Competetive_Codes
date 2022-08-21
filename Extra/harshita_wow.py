def AllCombination(arr, input1):
    dp=[[] for _ in range(input1+1)]
    for c in arr:
        for i in range(1,input1+1):
            if i < c:
                continue
            elif i==c:
                dp[i].append([c])
            elif i > c and dp[i-c]:
                for j in dp[i-c]:
                    dp[i].append(j+[c])
    print(dp)
    return sorted(dp[-1], key=lambda x:len(x))


def SieveOfEratosthenes(input1, input2):
    prime = [True for i in range(input1+1)]
    p = 2
    while (p * p <= input1):
        if (prime[p] == True):
            for i in range(p * p, input1+1, p):
                prime[i] = False
        p += 1
    
    arr = []
    for p in range(2, input1+1):
        if prime[p]:
            arr.append(p)
            
    return arr[:input2]

def sol(input1, input2):
    arr = SieveOfEratosthenes(input1, input2)
    res = AllCombination(arr, input1)
    if res:
        return len(res[0])
    else:
        return -1
            
if __name__ == "__main__":
    input1 = int(input())
    input2 = int(input())
    print(sol(input1, input2))