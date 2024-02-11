def sol(n, arr, num):
  count = 0
  for i in range(1,n):
    if (arr[i] + arr[i-1])%num == 0:
      count += 1
  return count

if __name__ == "__main__":
  n = int(input())
  l = int(input())
  arr = []
  for _ in range(l):
    arr.append(int(input()))
  print(sol(l, arr, n))