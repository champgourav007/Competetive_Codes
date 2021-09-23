arrang = input()

i=0
flag = 0
while i < len(arrang)-1:
    j = i+1
    if arrang[i] == arrang[j]:
        count = 0
        while j < len(arrang) - 1 and flag != 1:
            if arrang[i] == arrang[j]:
                count += 1
                if count >= 7:
                    print("YES")
                    flag  = 1
                    break
            else:
                i = j
                break
            j+=1
    else:
        i += 1
print("NO")
    