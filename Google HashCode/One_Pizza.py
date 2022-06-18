t = int(input())
likes = []
dislikes = []
for _ in range(t):
    l = input().split()
    d = input().split()
    n1 = int(l[0])
    for i in l[1:]:
        likes.append(i)
    n2 = int(d[0])
    for i in d[1:]:
        dislikes.append(i)
for i in dislikes:
    if len(i) != 0:
        count = likes.count(i)
        for j in range(count):
            likes.remove(i)
print(len(set(likes)), *set(likes))
