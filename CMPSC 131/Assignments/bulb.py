def bulbs():
    bulbs = []
    for i in range(100):
        bulbs.append("Off")
    return bulbs


def switch(bulbList):
    for x in range(100):
        factorList = []
        for i in range(1, bulbList.index(i)+1):
            if bulbList.index(i)%i == 0:
                factorList.append(bulbList.index(i))
                if len(factorList)%2 == 0:
                    bulbList[x] = "Off"
                if len(factorList)%2 == 1:
                    bulbList[x] = "On"
    return bulbList

if __name__ == "__main__":
    bulbList = bulbs()
    bulbList = switch(bulbList)
    print(bulbList)
    print(bulbList[63])
