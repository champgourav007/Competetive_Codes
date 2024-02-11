
from collections import defaultdict


factorial_dict = {
  0 : 1,
  1: 1,
  2: 2,
  3 : 6,
  4 : 24,
  5 : 120,
  6 : 720,
  7 : 5040,
  8 : 40320,
  9 : 362880
}

def NoOfDaySpecialDishToBeServed(arr, N):
  res = []
  for i in arr:
    flag = 0
    val = i
    prev_result = defaultdict(int)
    s = 0
    for j in range(60):
      if prev_result.get(val, False):
        break
      for k in str(val):
        s += factorial_dict.get(int(k))
      prev_result[val] = 1
      if s == int(i):
        res.append(j+1)
        flag = 1
        break
      val = s
      s = 0
    if not flag:
      res.append("F")
  return res
    
if __name__ == "__main__":
  food_items = list(map(int, input().split()))
  print(NoOfDaySpecialDishToBeServed(food_items, len(food_items)))