from collections import defaultdict

n, m = map(int, input().split())
nameDict = defaultdict(list)
for _ in range(n):
    name, skills = map(str, input().split())
    skills = int(skills)
    while skills:
        v = input().split()
        nameDict[v[0]].append([name, v[1]])
        skills-=1
# print(nameDict.items(),end="\n")
projectDict = defaultdict(list)
for _ in range(m):
    name, d, s, bb, l = map(str,input().split())
    l = int(l)
    req = l
    while l:
        v = input()
        projectDict[name].append([v.split(),[d,s,bb,req]])
        l-=1
print(projectDict)
while len(projectDict):
    prog, skill = [], []
    for i in projectDict.values():
        prog.append(i[0][0])
        skill.append(int(i[0][1]))
    score = 0
    for i in prog:
        if nameDict.get(i):
            score+= nameDict[i][1]    