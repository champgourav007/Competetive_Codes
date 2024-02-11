from collections import defaultdict


def sol(oldPassStr, newPassStr):
  d1 = defaultdict(int)
  for i in oldPassStr:
    d1[i] += 1
  d2 = defaultdict(int)
  for i in newPassStr:
    d2[i] += 1
  
  count = 0
  for i,j in d1.items():
    if d2.get(i):
      count += abs(d2.get(i) - j)
      d2[i] = 0
      d1[i] = 0
  
  for i in d1.values():
    if i != 0:
      count += i
  
  for i in d2.values():
    if i != 0:
      count += i
  
  return count

if __name__ == "__main__":
  pass1 = input()
  pass2 = input()
  print(sol(pass1, pass2))