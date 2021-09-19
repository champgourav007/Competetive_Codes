test_cases = int(input())
while test_cases > 0:
    g,c = map(int,input().split())
    h = (c**2)//(2*g)
    print(h,end="\n")
    test_cases -= 1
