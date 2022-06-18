def sol(st, pref):
    res = {}
    for i in st:
        for j in i[1][1:]:
            clg = int(j[2:])
            if pref.get(clg, 0) != 0:
                pref[clg] -= 1
                res[i[0]] = j
                break
    return res


if __name__ == "__main__":
    c,n = map(int,input().split())
    clg_dict = {}
    clg = list(map(int, input().split()))
    for i in range(1, c+1):
        clg_dict[i] = clg[i-1]
    st = {}
    for i in range(1, n+1):
        s = list(map(str, input().split(",")))
        st[s[0]] = s[1:]
    v = sorted(st.items(), key= lambda x : float(x[1][0]), reverse = True)
    print(v)
    result = sol(v, clg_dict)
    for i,j in result.items():
        print(f"{i} {j}")

        
    