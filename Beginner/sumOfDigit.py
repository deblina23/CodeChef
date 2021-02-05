#!/usr/bin/env python3
def readInput():
    totalTestCase = int(input())
    numberList = []
    if((totalTestCase>=1) and (totalTestCase<=1000)):
            for number in range(0,totalTestCase):
                numberList.append(input())
            return(numberList)
    else:
        return(numberList)

def sumOfDigit(numberList):
    sumList = []
    if (len(numberList)>0):
        for numbers in numberList:
            digits =[int(n) for n in str(numbers)]
            sumList.append((sum(digits)))
    return(sumList)
def printResult(sumList):
    for result in sumList:
        print(result)
if __name__ == "__main__":

    numberList = readInput()
    sumList = sumOfDigit(numberList)
    printResult(sumList)
    

    



