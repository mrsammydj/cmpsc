#Ask for amount of grades and values
loopAmount = int(input("How many grades do you want to enter: "))
loopCount = 0
numGradeFinal = 0
letterGrade = "F"
passing = True
while loopCount < loopAmount:
    loopCount += 1
    numGrade = float(input("Enter grade #" + str(loopCount) + ": "))
    numGradeFinal += numGrade
numGradeFinal = numGradeFinal/loopAmount
print(numGradeFinal)

#If statements establishing letter grade
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

if numGradeFinal >= 70:
    passing = True
else:
    passing = False


#Print results
if numGradeFinal > 90 or numGradeFinal < 60:
    print("You got an " + letterGrade)
else:
    print("You got a " + letterGrade)

if passing == True:
    print("You passed!")
else:
    print("You failed!")