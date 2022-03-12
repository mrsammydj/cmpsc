#Function converting minutes to seconds
def minToSec(min):
    sec = min*60
    return sec

#Function converting hours to seconds
def hourToSec(hour):
    min = hour*60
    sec = minToSec(min)
    return sec

#Function that calculates points based on team's record
def pointsFunc(win, loss, otLoss):
    points = (win*2) + (otLoss)
    return points

#Print the different options
def menuOptions():
    print("Option 1: A function converting minutes to seconds\n")
    print("Option 2: A unction converting hours to seconds\n")
    print("Option 3: A function that calculates points based on team's record.\nWin = 2 pts, Loss = 0 pts, OT Loss = 1 pt.\n")

#Main function
def main():
    menuOptions()
    selection = int(input("Please input a function that you wish to use (1, 2, or 3). "))

    if selection == 1:
        min = int(input("Enter an amount of minutes: "))
        sec = minToSec(min)
        print(min,"minutes is",sec,"seconds.")
    if selection == 2:
        hour = int(input("Enter an amount of hours: "))
        sec = hourToSec(hour)
        print(hour,"hours is",sec,"seconds.")
    if selection == 3:
        win = int(input("Input the amount of wins: "))
        loss = int(input("Input the amount of losses: "))
        otLoss = int(input("Input the amount of OT Losses: "))
        points = pointsFunc(win, loss, otLoss)
        print("The team's record is", points, "points")

main()
