n,x = map(int,input().split())
s = input()
string = [i for i in s]
size = len(string)

while x:
    i = 0
    j = i+1
    while j < size:
        if string[i] == 'B' and string[j] == 'G':
            temp = string[i]
            string[i] = string[j]
            string[j] = temp
            i = j+1
            j = i+1
        else:
            i += 1
            j = i+1
    x-=1
print(*string,sep="")