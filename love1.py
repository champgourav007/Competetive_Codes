import math

def sol(n, arr):
  count = 0
  for i in arr:
    if i > 0:
      val = math.sqrt(i)
      if int(val) * int(val) == i:
        count += 1
  return count

if __name__ == "__main__":
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(int(input()))
  print(sol(n, arr))