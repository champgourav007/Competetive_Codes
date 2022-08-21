a, b, c = 0, 1, 1
while True:
    b = b*c
    a=a+(b//c)
    c = c+1
    if c == 10:
        break
print(a)