from collections import defaultdict

if __name__ == "__main__":
  n = int(input())
  res = defaultdict(int)
  for i in range(n):
    val = int(input())
    res[val] += 1
  count = 0
  for value in res.values():
    if value % 2 != 0:
      count += 1
  print(count)
    