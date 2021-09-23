string = input()
vowels = "aeiouy"
res = ""
for i in string:
    if i.lower() in vowels:
        continue
    elif i == " ":
        continue
    else:
        res += "." + i.lower()
print(res)