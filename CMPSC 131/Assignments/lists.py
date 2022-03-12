
def loop(loopAmount):
    scores = []

    for i in range(loopAmount):
        score = float(input("Enter grade #" + str(i+1) + ": "))
        maxScore = float(input("Enter the maximum possible points for this assignment: "))
        scoreType = int(input("Enter the type of assignment: "))
        print("\n")
        scores.append([i, score, maxScore, scoreType])

    return scores

def averageScore(scores, t):
    _sum = 0
    total = 0
    for s in scores:
        _sum += s[1]
        total += s[2]
    
    if total == 0:
        return 0
    
    return (_sum/total)*100

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

def passFail(avg):
    print("You passed!" if avg >= 70 else "You failed!")

if __name__ == "__main__":
    typePercs = [.4, .25, .1, .25]
    loopAmount = int(input("How many grades do you want to enter: "))
    scores = loop(loopAmount)
    totalGrade = 0
    for i in range(len(typePercs)):
        totalGrade += averageScore(scores, i)*typePercs[i]

    letter = getLetterGrade(totalGrade)
    print("Letter Grade = "+letter)
    passFail(totalGrade)
