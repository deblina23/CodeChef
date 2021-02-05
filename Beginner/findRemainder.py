#!/usr/bin/env python3
def readInputAndLogicUnit():
        totalTestcase = int(input())
        resultList = []
        if(checkRange(totalTestcase,1,1000)):
            for number in range(0,totalTestcase):
                number1,number2 = map(int,(input().split()))
                if((checkRange(number1,1,10000)) and (checkRange(number2,1,10000))):
                    result =(number1%number2)   
                    resultList.append(result)
        return(resultList)

def printModule(resultSet):
    for result in resultSet:
        print(result)

def checkRange(value, minValue,maxValue):
    if(value in range(minValue,maxValue)):
            return(True)
    else:
        return(False)
        
if __name__ == "__main__":

    resultSet = readInputAndLogicUnit()
    printModule(resultSet)
