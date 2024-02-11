
def sol(h, m, h1, m1, x):
  current_time = h + x
  current_min = (current_time * 60) + m
  new_min = (h1 * 60) + m1
  return current_min - new_min

if __name__ == "__main__":
  h = int(input())
  m = int(input())
  h1 = int(input())
  m1 = int(input())
  x = int(input())
  print(sol(h,m,h1,m1, x))