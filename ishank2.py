def fill_test_tube(x, y, z):
  a = 0
  c = 0
  b = x+y
  while c != z:
    if a == 0:
      if c >= x:
        c -= x
        a = x
      else:
        a = c
        c = 0

    if c + a <= y:
      c += a
      a = 0
    else:
      a -= (y - c)
      c = y
    if c == z:
      return "YES"

    if a > 0 and x+y-z >= c+a:
      b = x+y-z-c
      if b >= a:
        c += a
        a = 0
      else:
        a -= b
        c += b
      if c == z:
        return "YES"

    if c < z and b > 0:
      if c+b <= z:
        c += b
        b = 0
      else:
        b -= (z-c)
        c = z
      if c == z:
        return "YES"

    if a == 0 and b == 0 and c != z:
      return "NO"
  return "YES"



if __name__ == "__main__":
  x, y = map(int, input().split())
  z = int(input())
  print(fill_test_tube(x, y, z))
