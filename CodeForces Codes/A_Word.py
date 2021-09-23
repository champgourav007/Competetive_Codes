string = input()
count_upper = 0
count_lower = 0
for i in string:
    if i >= 'A' and i <= 'Z':
        count_upper += 1
    else:
        count_lower += 1
if count_lower >= count_upper:
    print(string.lower())
else:
    print(string.upper())