from itertools import combinations_with_replacement
def solve(input1,input2,input3):
    p=[x for x in range(input2,input3+1)]
    com=[]
    for i in range(1,input1+1):
        com=com+list(combinations_with_replacement(p,i))
    return len(com)

if __name__ == "__main__":
  n = int(input())
  start = int(input())
  end = int(input())
  solve(n, start, end)
  