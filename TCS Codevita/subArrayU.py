
def mNtime(m,n):
    if(n==0):
        return 1
    return m*mNtime(m-1,n-1)


def div(n,r):
    return mNtime(n,r)/mNtime(r,r)

def sol():
    pad=0
    for ti in range(sublargeText):
        pad+=div(largeText,ti)
    def padInSubSet(text,subtext):
        if(len(subtext)==0):
            return 1
        largeText,sublargeText=len(text),len(subtext)
        pad=0
        for _ in range(largeText-sublargeText+1):
            if(text[_]!=subtext[0]):
                pad+=div(largeText-_-1,sublargeText-1)
            else:
                pad+=padInSubSet(text[_+1:],subtext[1:])
                break;
        return pad
    pad+=padInSubSet(text,subtext)
    print(int(pad))


if __name__ == "__main__":
    n=int(input())
    subtext=input().split(",")
    text = input().split(",")
    largeText=len(text)
    sublargeText=len(subtext)
    sol(subtext, largeText, )