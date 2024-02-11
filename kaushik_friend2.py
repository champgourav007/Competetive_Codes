from collections import defaultdict, deque

def numOfFriends(N, M, friend):
  friend_dict = defaultdict(list)
  for i,j in friend:
    friend_dict[i].append(j)
  queue = deque()
  already = defaultdict(int)
  queue.append([friend[0][0]])
  already[friend[0][0]] = 1
  count, res = 0, 0
  while len(queue):
    val = queue.popleft()
    print(val, "14")
    for i in val:
      if already.get(i):
        res = max(count, res)
      already[i] = 1
      queue.append(friend_dict[i])
    count += 1
  return res
    

if __name__ == "__main__":
  n = int(input())
  follower = int(input())
  arr = []
  for _ in range(follower):
    rel = list(map(int, input().split()))
    arr.append(rel)
  print(numOfFriends(n, follower, arr))