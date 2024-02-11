def sol(input_from_question):
    s = input_from_question
    vowelsDict = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
    res = ""
    for i in s:
        if i >= 'a' and i <= 'z':
            val = ord(i)
            if val+1 >= 123:
                val = 97 + (val%122)
            else:
                val += 1
            if vowelsDict.get(chr(val), None) != None:
                res += chr(val).upper()
            else:
                res += chr(val)
        else:
            res += i
    return res
            

if __name__ == "__main__":
    input_from_question = input()
    print(sol(input_from_question))