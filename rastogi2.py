def sol(values, rows, cols):
  mini_arr = [float("inf")]*cols
  for i in range(cols):
    for j in range(rows):
      if values[j][i] == -1:
        continue
      mini_arr[i] = min(values[j][i], mini_arr[i])
  
  for i in range(rows):
    for j in range(cols):
      if values[i][j] == -1:
        values[i][j] = mini_arr[j]
  return values

if __name__ == "__main__":
  n, m = map(int, input().split())
  arr = []
  for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
  print(*sol(arr, n, m))