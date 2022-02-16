def isPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True

def factors(val):
    count = 0
    for i in range(1,val+1):
        if val%i == 0:
            count+=1
    return count

string = input().split()
val = 0
for i in string:
    if i.isdigit():
        val += int(i)%10
if val == 0:
    print(-1)
else:
    if isPrime(val):
        print(val)
    val = str(val)
    rev = val[::-1]
    if isPrime(int(rev)):
        print(int(rev))
    else:
        print(factors(int(rev)))

