

string = input()
vowels = "aeiou"
v = []
for i in string:
    if i.lower() in vowels:
        v.append(i)
new_v = v[::-1]
res = []
for i in string:
    if i not in v:
        res.append(i)
    else:
        res.append(new_v.pop(0))

res = ''.join(i for i in res)
print(res)

if __name__ == "__main":
    a = input()
