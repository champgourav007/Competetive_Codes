from collections import defaultdict


def sol(n, q, a, query):
  count_dic = defaultdict(int)
  for i in a:
    count_dic[i] += 1
  
  res = []
  for i in query:
    val = count_dic.get(i)
    if val:
      res.append(val)
    else:
      val1 = count_dic.get(i-1)
      val2 = count_dic.get(i+1)
      if val1 and val2:
        res.append(max(val1, val2))
      elif val1:
        res.append(val1)
      elif val2:
        res.append(val2)
      else:
        res.append(0)
  return res

if __name__ == "__main__":
  n, q = map(int, input().split())
  a = list(map(int, input().split()))
  query = list(map(int, input().split()))
  print(*sol(n, q, a, query))