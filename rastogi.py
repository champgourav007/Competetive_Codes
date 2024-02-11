def sol(x, y):
  tot_cost = 0
  for i in range(x, y+1):
    val1 = str(i)
    val2 = [int(val) for val in val1]
    maxi = max(val2)
    s = sum(val2)
    if s-int(maxi) == int(maxi):
      s+=1
      continue
    tot_cost += i
  return tot_cost
    

if __name__ == "__main__":
  x, y = map(int, input().split())
  print(sol(x, y))