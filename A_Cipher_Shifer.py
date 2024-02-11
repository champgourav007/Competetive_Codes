def sol(n, s):
  if n <= 0:
    return ""
  val = s[0]
  i = 1
  res = ""
  while i < n:
    if val == s[i]:
      res += val
      val = s[i+1] if i != n-1 else ""
      i+=1
    i+=1
  return res

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    print(sol(n, s))