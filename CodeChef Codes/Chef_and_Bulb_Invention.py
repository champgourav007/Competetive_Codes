def bulbs():
    n,p,k = map(int,input().split())
    val1 = (n-1)%k
    val2 = (n-1)//k
    val3 = p%k
    if(val1>=val3):
        res = val3 * (val2 + 1)
    else:
        res = ((val1+1)*(val2+1)) + (val3-val1-1)*val2
    res += (p//k)+1
    return int(res)
        
        
                
                
                

if __name__ == "__main__":
    test_cases = int(input())
    while test_cases > 0:
        ans = bulbs()
        print(ans)
        test_cases-=1