n = int(input())
rem = n%5
count = n//5
if rem != 0:
    print(count+1)
else:
    print(count)
