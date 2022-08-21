from collections import defaultdict

def sol(s):
    count = defaultdict(int)
    keypad = {}
    for i in range(1,10):
        keypad[i] = set()
    check = defaultdict(int)
    val = 1
    for i in s:
        if not check.get(i):
            if val%10 == 0:
                val = 1
            else:
                val = val%10
            string = keypad[val]
            while len(string) >= 3:
                val += 1
                string = keypad[val] 
            string.add(i)
            keypad[val] = string
            check[i] = [1, len(string)]
            val += 1
    for i in s:
        count[i] += 1
    res = 0
    string = set(s)
    for i in string:
        res += count[i] * check[i][1]
    return res
    
    
    
        

if __name__ == "__main__":
    string = input()
    print(sol(string))