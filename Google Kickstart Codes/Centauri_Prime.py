def sol(s):
    n = len(s)
    vowels = "aeiouAEIOU"
    ex = "yY"
    if s[n-1] in vowels:
        return "Alice"
    elif s[n-1] not in ex:
        return "Bob"
    else:
        return "nobody"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = input()
        print("Case #" + str(i+1) + ": " + string + " is ruled by " + sol(string) + ".")
