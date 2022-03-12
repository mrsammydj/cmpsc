def groupingOdds(numbers):
    oddList = []
    for i in numbers:
        if i%2 != 0:
            oddList.append(i)
    return oddList

numList = [1, 2, 5, 7, 8, 9]
odds = groupingOdds(numList)
print(odds)