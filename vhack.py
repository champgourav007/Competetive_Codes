def sol(n, m, k, prod_asmbly, c, z, red):
  for i in range(z):
    rem = {val+1 : c[val] for val in range(0,m)}
    count = {}
    for x, y in prod_asmbly:
      if rem[y] > 0 and count.get(x, 0) == 0:
          count[x] = 1
          rem[y]-=1
    print(len(count))
    c[red[i][0]-1] -= red[i][1]


if __name__ == "__main__":
  n, m, k = map(int, input().split())
  prod_asmbly = []
  for i in range(k):
    prod_asmbly.append(list(map(int, input().split())))
  c = list(map(int, input().split()))
  z = int(input())
  red = []
  for i in range(z):
    red.append(list(map(int, input().split())))
  sol(n, m, k, prod_asmbly, c, z, red)