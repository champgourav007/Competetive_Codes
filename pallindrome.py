def isPallindrome(a):
    rev = a[::-1]
    if rev == a:
        return True
    return False


def sol(last, arr, n):
    count = 0
    for j in range(n - last + 1):
        if isPallindrome(arr[j:j+last]):
            count+=1
    return count


if __name__ == "__main__":
    n = int(input())
    arr = input()
    m = int(input())
    pos = list(map(int, input().split()))
    res = 0
    for i in range(m):
        res += sol(pos[i], arr, n)
    print(res)