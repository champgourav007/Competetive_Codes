# c,n = map(int,input().split())
# req = dict()
# req_clg = list(map(int, input().split()))
# for i in range(c):
#     req[i+1] = req_clg[i]
# stud = dict()
# for i in range(n):
#     s = list(map(str, input().split(",")))
#     stud[s[0]] = s[1:]
# sorted_student = sorted(stud.items(), key = lambda x : float(x[1][0]), reverse = True)
# res = {}
# for i in sorted_student:
#     for j in i[1][1:]:
#         clg = int(j[2:])
#         if req.get(clg, 0) != 0:
#             req[clg] -= 1
#             res[i[0]] = j
#             break
# for i,j in res.items():
#     print(str(i) +" "+ str(j))


def allocate(clg):
    flag = 0
    for x in clg:
        for y in range(len(seats)):
            if seats[int(x[2:])-1] and seats[int(x[2:])-1] != 0:
                seats[int(x[2:])-1] -= 1
                flag = 1
                break
        if flag == 1:
            return [True,x]
    return [False]

C, N = map(int, input().split())
seats = list(map(int,input().split()))
students = []
output = []
for x in range(N):
    students.append(input().split(','))
students = sorted(students, key=lambda x : float(x[1]), reverse=True)
for x in students:
    val = allocate(x[2:])
    if val[0]:
        print(x[0],val[1])