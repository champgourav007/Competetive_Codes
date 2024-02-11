def sol(pallindromeStr):
    n = len(pallindromeStr)
    if n == 1:
        return ""
    res, flag =[pallindromeStr[n//2]]*n, 0
    for i in range(n//2):
        if not flag and pallindromeStr[i] != 'a':
            res[i] = 'a'
            flag = 1
        else:
            res[i] = pallindromeStr[i]
        res[n-i-1] = pallindromeStr[i]
    return "".join(res)

if __name__ == "__main__":
    pallindromeStr = input()
    print(sol(pallindromeStr))