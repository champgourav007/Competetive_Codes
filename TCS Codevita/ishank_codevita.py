from collections import defaultdict, OrderedDict
if __name__ == "__main__":
    teams = ["MI","CSK","RCB","RR","SRH","DC","PBKS","KKR"]
    points = defaultdict(int)
    nrr = defaultdict(int)
    s1 = 7
    print()
    while s1:
        s = list(map(str, input().split()))
        balls1 = int(s[2])
        balls2 = int(s[5])
        score1 = int(s[1].split("/")[0])
        score2 = int(s[4].split("/")[0])
        flag = 0
        win = 0
        if score1 == score2:
            points[s[0]] += 1
            points[s[3]] += 1
            flag = 1
        elif score1 > score2:
            points[s[0]] += 2
            win = 0
        else:
            points[s[3]] += 2
            win = 1
        if flag == 0:
            if win == 0:
                dif = score1 - score2
                rr = dif*0.05
                nrr[s[0]] += rr
                nrr[s[3]] -= rr
            else:
                pr = score2*120/ balls2;
                rr = (pr-score1)*0.05
                nrr[s[3]] += rr
                nrr[s[0]] -= rr
        s1-=1
    po = sorted(points.items(), key = lambda x : x[1])
    points = defaultdict(int)
    for i,j in po:
        points[i] = j
    p = [0]*8
    st = [0]*8 
    i=0
    for key,value in points.items():
        p[i] = value
        st[i] = key
        i+=1
    srt = defaultdict()
    for i in range(7,0,-1):
        if p[i] == p[i-1]:
            srt[nrr[st[i]]] = st[i]
        else:
            if len(srt) == 0:
                print(st[i],end=" ")
            else:
                srt[nrr[st[i]]] = st[i]
                nk = sorted(srt.items(), key = lambda x : x[0], reverse=True)
                for i,j in nk:
                    print(j,end=" ")
                srt.clear()
        # print(srt)
        if i == 0:
            print(st[0],end=" ")
        elif len(srt)!=0:
            nk = sorted(srt.items(), key = lambda x : x[0], reverse=True)
            for i,j in nk:
                    print(j,end=" ")
    
            

                
                
    


