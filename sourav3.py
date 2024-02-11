def sol(l, r):
    if l == r:
        return [1,1]
    if r%2 != 0 and l%2 != 0:
        return [l, r-2]
    if r%2 == 0 and l%2 != 0:
        return [l, r]
    elif r%2 != 0 and l%2 == 0:
        return[l, r]
    else:
        return [l, r-1]
        

if __name__ == "__main__":
    l = int(input())
    r = int(input())
    print(sol(l ,r))