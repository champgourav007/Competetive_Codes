def sol(n, a):
  if n == 2:
    return a[0] * a[1]
  
  max_neg1 = -float("inf")
  max_pos1 = -float('inf')
  obt = [-1, -1]
  for i in range(n):
    if a[i] < 0 and max_neg1 < abs(a[i]):
      max_neg1 = abs(a[i])
      obt[0] = i
    if a[i] > 0 and max_pos1 < a[i]:
      max_pos1 = a[i]
      obt[1] = i
  
  # print(obt)
  max_pos2 = -float("inf")
  max_neg2 = -float("inf")
  for i in range(n):
    if a[i] < 0 and max_neg2 < abs(a[i]) and obt[0] != i:
      max_neg2 = abs(a[i])
      # obt[0] = i
    if a[i] > 0 and max_pos2 < a[i] and obt[1] != i:
      max_pos2 = a[i]
      # obt[1] = i
      
  # print(obt)
  if max_neg1 == -float("inf"):
    max_neg1 = 0
  if max_pos1 == -float("inf"):
    max_pos1 = 0
  if max_neg2 == -float("inf"):
    max_neg2 = 0
  if max_pos2 == -float("inf"):
    max_pos2 = 0
  return max(max_neg1 * max_neg2, max_pos1 * max_pos2)
  
      

if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(sol(n, a))