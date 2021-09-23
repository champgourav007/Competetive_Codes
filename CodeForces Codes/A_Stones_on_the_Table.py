size = int(input())
arrang = input()
i = 0
count = 0
while i < size:
    j = i+1
    while j < size:
        if arrang[i] == arrang[j]:
            count += 1
        else:
            break
        j += 1
    if j == size:
        break
    i += 1 
print(count)