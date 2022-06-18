def solution(s,t):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            print("New Language Error")
            break
    else:
        l=[]
        for j in t:
            k=""
            for i in s:
                b=j.count(i)
                if i in j:
                    while b>0:
                        k+=i
                        b-=1
            l.append(k)
        for i in l:
            print(i,end=" ")


def main():
    s=input().lower()
    t=list(input().lower().split())
    solution(s,t)



if __name__ == "__main__":
    main()
