t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count1 = s.count('1')
    count0 = s.count('0')
    if count1 == 0 or count0 == 0:
        print(1)
        continue
    v = min(count1, count0)
    if count1 == count0:
        res = v*2
    else:
        res = v*2+1
    print(res)