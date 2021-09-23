s = input()
size = len(s)
i = 0
j = i+1
string = ""
while j < len(s):
    if s[i] == ".":
        string += "0"
        i = j
        j = i+1
    elif s[i] == "-" and s[j] == ".":
        string += "1"
        i = j+1
        j = i+1
    elif s[i] == "-" and s[j] == "-":
        string += "2"
        i = j+1
        j = i+1
while i < len(s):
    if s[i] == ".":
        string += "0"
    i+=1
print(string)