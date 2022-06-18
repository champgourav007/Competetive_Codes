def sol(students, clg):
    res = {}
    rem_student = []
    for i in students:
        v = i[1][1:]
        flag = 0
        for j in v:
            c = int(j[2])
            if clg.get(c, 0):
                clg[c] -= 1
                res[j] = float(i[1][0])
                flag = 1
                break
        if flag == 0:
            rem_student.append(i)
    for i in rem_student:
        for j,k in sorted(sorted(clg.items(), key = lambda x : x[0]), key=lambda x:x[1], reverse=True):
            if k != 0:
                c = 'C-'+str(j)
                res[c] = float(i[1][0])
                clg[j] -= 1
                break
    for i,j in clg.items():
        c = 'C-'+str(i)
        if c not in res:
            res[c] = 'n/a'
    return res

if __name__ == "__main__":
    c,n = map(int, input().split())
    clg = list(map(int, input().split()))
    print(clg)
    clg_dict = {}
    for i in range(1, c+1):
        clg_dict[i] = clg[i-1]
    students = {}
    for i in range(n):
        s = list(map(str, input().split(",")))
        students[s[0]] = s[1:]
    
    students = sorted(students.items() , key = lambda x : float(x[1][0]), reverse=True)
    result = sol(students, clg_dict)
    for i,j in result.items():
        print(f"{i} {j}")