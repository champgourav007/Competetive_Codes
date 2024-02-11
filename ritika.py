def sol(noOfDigitsForPallindrome, userId, password):
    fixed_users = {
        "user1" : "pass1",
        "user2" : "pass2",
        "user3" : "pass3",
        "user4" : "pass4",
        "user5" : "pass5",
    }

    if password != fixed_users.get(userId):
        return "UserId and password is not valid, pls try again."
    else:
        result = "Welcome " + userId + " and generated token is: " 
        token = "token-"
        if noOfDigitsForPallindrome % 2 == 0:
            if noOfDigitsForPallindrome == 2:
                return result + token + "11."
            else:
                return result + token + "1" + "0"*(noOfDigitsForPallindrome-2) + "1."
        else:
            if noOfDigitsForPallindrome == 1:
                return result + token + "1."
            else:
                return result + token + "1" + "0"*(noOfDigitsForPallindrome-2) + "1."

if __name__ == "__main__":
    noOfDigitsForPallindrome = int(input())
    userId = input()
    password = input()
    print(sol(noOfDigitsForPallindrome, userId, password))