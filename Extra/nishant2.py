n,d = map(int, input().split())
s = list(map(int, input().split()))
res = s[d:] + s[:d]
print(res)

