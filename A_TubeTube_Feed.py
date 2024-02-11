def sol(n, t, a, b):
  m = 0
  res = -1
  for i in range(n):
    if (b[i] > m) and t >= a[i]:
      m = b[i]
      res = i+1
    t-=1
  return res
    


if __name__ == "__main__":
  q = int(input())
  for _ in range(q):  
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sol(n, t, a, b))
  