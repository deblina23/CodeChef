def readInput():
    factorList = []
    for _ in range(int(input())):
        factorList.append(int(input()))
    return(factorList)

def calculateFactor(inputList):

    resultList = []
    for value in inputList:
        result = 1
        for pos in range (1,value+1):
            result = result*pos
        resultList.append(result)
    return(resultList)

def printResult(resultList):

    for data in (resultList):
        print(data)

if __name__ == "__main__":
    inputList=readInput()
    resultList = calculateFactor(inputList)
    printResult(resultList)
