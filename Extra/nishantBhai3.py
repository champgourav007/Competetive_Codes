n = int(input())
string = input()
vowels = "AEIOU"
res = []
for i in range(n):
    if string[i] not in vowels:
        res.append(string[:i] + " " + string[i:])
    else:
        res.append(string[:])

print(sorted(res))