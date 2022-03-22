t = int(input())
for _ in range(t):
    s = input()
    for i in range(len(s)):
        if s[i] not in s[i+1:]:
            break
    print(s[i:])