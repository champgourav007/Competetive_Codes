import collections
def sol(a, b):
    m = collections.defaultdict(str)
    minChr = 'z'
    for i in range(len(a)):
        if a[i] != b[i]:
            if m.get(a[i]):
                if m.get(a[i]) != b[i]:
                    return -1
            m[a[i]] = b[i]
            minChr = min(minChr, a[i])
    newA = list(m.keys())
    newB = list(m.values())
    count = 0
    for i in range(len(newA)):
        if newA[i] != newB[i]:
            count += 1
            newA[i] = minChr
    if newA == newB:
        return minChr
    return -1

if __name__ == "__main__":
    a = input()
    b = input()
    print(sol(a, b))