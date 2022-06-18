def solution(n):
    res = 1
    res += n
    res *= (n+1)/2
    return res

n = int(input())
print(solution(n))