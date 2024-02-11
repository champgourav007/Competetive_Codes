def check_email(email):
    email = email.replace("_","")
    if email.find("@") != -1  or email.find(".") != -1:
        return False
    if email[-1] in "@.":
        return False
    if email[0] in "@.":
        return False
    print(email.find(" "))
    if email.find(" ") != -1:
        return False
    posAt = email.find("@")
    posDot = email.find(".")
    if abs(posAt - posDot) <= 1:
        return False
        
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        email = input()
        print(check_email(email))
        