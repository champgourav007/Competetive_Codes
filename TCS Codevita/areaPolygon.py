if __name__ == "__main__":
    t = int(input())
    ans, isX, isY, anti, prop = -1, True, True, 1e6, 1e8
    for i in range(t):
        x,y = map(int, input().split())
        if isX is True and x == anti and y != prop:
            anti = x
            prop = y
            isX = False
            isY = True
            ans+=1
        elif isY is True and y == prop and x != anti:
            anti = x
            prop = y
            isY = False
            isX = True
            ans+=1
        elif y != prop and x != anti:
            anti = x
            prop = y
            isX = True
            isY = True
            ans+=1
        else:
            anti = x
            prop = y
    print(ans+1)
