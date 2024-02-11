def sol(n, arr):
    if n == 1:
        return "YES"
    else:
        for i in range(1, n):
            if (arr[i]%2 == arr[i-1]%2):
                return "NO"
        return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            val = int(input())
            arr.append(val)
        print(sol(n, arr))