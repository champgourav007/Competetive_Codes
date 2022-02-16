t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    p = input()
    consonants = {'b':1, 'c':1, 'd':1, 'f':1, 'g':1, 'h':1, 'j':1, 'k':1, 'l':1,
                  'm':1, 'n':1, 'p':1, 'q':1, 'r':1, 's':1, 't':1, 'v':1, 'w':1, 'x':1, 'y':1, 'z':1}
    vowels = {'a':2,'e':2,'i':2,'o':2,'u':2}
    mini = float("inf")
    for i in range(26):
        count = 0
        char = chr(97+i)
        j = 0
        temp_p = [i for i in p]
        temp_s = [i for i in s]
        while j <  n:
            if temp_s[j] == '?':
                temp_s[j] = char
            if temp_p[j] == '?':
                temp_p[j] = char
            if temp_s[j] != temp_p[j]:
                con_s = consonants.get(temp_s[j])
                vow_s = vowels.get(temp_s[j])
                con_p = consonants.get(temp_p[j])
                vow_p = vowels.get(temp_p[j])
                pos_s = con_s if con_s is not None else vow_s
                pos_p = con_p if con_p is not None else vow_p
                if pos_s != pos_p:
                    count+=1
                else:
                    count+=2
            j+=1
        mini = min(count,mini)
    print(mini)