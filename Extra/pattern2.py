n = int(input())
res = ""
for i in range(n+1):
    char = chr(65+i)
    if i == 0:
        print(char)
        res = char
        continue
    res = char + res + char