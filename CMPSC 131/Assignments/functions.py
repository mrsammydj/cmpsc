#Ask for amount of grades and values
numGrade = 0
letterGrade = str("F")
passing = True
loopAmount = int(input("How many grades do you want to enter: "))

def loop(loopAmount,numGrade):
    for i in range(loopAmount):
        grade = float(input("Enter grade #" + str(i+1) + ": "))
        numGrade += grade
    return numGrade

#If statements establishing letter grade
def getLetterGrade(numGradeFinal):
    if numGradeFinal >= 93: 
        letterGrade = "A"
    elif numGradeFinal > 90:
        letterGrade = "A-"
    elif numGradeFinal > 87:
        letterGrade = "B+"
    elif numGradeFinal > 83:
        letterGrade = "B"
    elif numGradeFinal > 80:
        letterGrade = "B-"
    elif numGradeFinal > 76:
        letterGrade = "C+"
    elif numGradeFinal > 70:
        letterGrade = "C"
    elif numGradeFinal > 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    return letterGrade

def passOrFail(numGradeFinal):
    if numGradeFinal >= 70:
        print("You passed!")
    else:
        print("You failed!")


numGradeFinal = loop(loopAmount,numGrade)/loopAmount
print(numGradeFinal)
letterGrade = str(getLetterGrade(numGradeFinal))


#Print results
if numGradeFinal > 90 or numGradeFinal < 60:
    print("You got an " + str(letterGrade))
else:
    print("You got a " + str(letterGrade))

passOrFail(numGradeFinal)
