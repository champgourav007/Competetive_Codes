from distutils.log import error


# Input Format:-

#     10
#     GT 20 T T F F T
#     LSG 18 T F F T T
#     RR 16 T F T F F
#     DC 14 T T F T F
#     RCB 14 F T T F F
#     KKR 12 F T T F T
#     PBKS 12 F T F T F
#     SRH 12 T F F F F
#     CSK 8 F F T F T
#     MI 6 F T F T T
#     F 2   



#userdefined Exception
class losswinERROR(Exception):
    pass

#function to calculate the average
def calAverage(teams, teams_dict):
    points = 0

    for i in teams:
        points += teams_dict.get(i)["points"]
    
    return points/len(teams)


#function to check the teams for the given win or loss
def check(teams_dict, lossORwin, value):
    res_team = []

    for team_name, team_values in teams_dict.items():

        performance = team_values.get("performance")
        count = 0

        for i in performance:
            
            if i == lossORwin:
                count += 1

            elif i != lossORwin:
                count = 0

            if count >= value:
                res_team.append(team_name)
                break

    if len(res_team) > 0:
        avg = calAverage(res_team, teams_dict)

    else:
        print("No teams!!")
        avg = 0

    return {
        "avg" : avg,
        "teams" : res_team,
    }



#main function
if __name__ == "__main__":

    n = int(input())
    teams = []

    for _ in range(n):
        team = list(map(str, input().split())) #it will take input in "NAME POINTS 5-Consecutive Performance"
        teams.append(team)

    try:
        lossORwin, value = map(str, input().split()) #enter "T" for win or enter "F" for Loss

        if lossORwin not in "TF":
            raise losswinERROR

    except losswinERROR:
        error("Please enter 'T' for WIN or 'F' for LOSS ")

    except:
        error("Please enter some positive integer for loss and win!!!!")

    teams_dict = {}

    for i in teams:
        try:
            teams_dict[i[0]] = {
                "points" : int(i[1]),
                "performance" : i[2:],
            }

        except:
            error(f"Points should be integer, and you have enter : {i[1]}")

    data = check(teams_dict, lossORwin, int(value))

    if lossORwin == "T":
        lossORwin = "WIN"

    else:
        lossORwin = "LOSS"

    print(f"The teams having consecutive {lossORwin} are", *data.get("teams"), " and average score is ", data.get("avg"))
    

