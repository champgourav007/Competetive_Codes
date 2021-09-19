test_cases = int(input())
while test_cases > 0:
    d,x,y,z = map(int,input().split())
    first_work = x*7
    second_work = d*y + (7-d)*z
    print(max(first_work,second_work))
    test_cases-=1