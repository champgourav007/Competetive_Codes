year = int(input())
# print(year%10,(year//10)%10,(year//100)%10,(year//1000)%10)
temp = year
while True:
    temp  += 1
    year = temp
    if year % 10 != (year//10)%10 and year % 10 != (year//100)%10 and year % 10 != (year//1000)%10:
        year = year//10
        if year % 10 != (year//10)%10 and year % 10 != (year//100)%10:
            year = year//10
            if year % 10 != (year//10)%10:
                break
print(temp)

    