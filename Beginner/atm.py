#!/usr/bin/env python3
def readInput():
    inputLine = input()
    return( inputLine)

def logicUnit(inputData):
    amount, totalBalance = [float(n) for n in inputData.split()]
    if((amount>0.0) and (amount<=2000.0) and ((amount%5) == 0)):
        if((totalBalance>0.00) and (totalBalance <= 2000.00) and (totalBalance>amount)):
            totalBalance = totalBalance-amount
            finalBalance = float(totalBalance)-0.5
            return(finalBalance)
        else:
            return(totalBalance)
    else:
        return(totalBalance)

def printData(finalValue):
    print(finalValue)

if __name__ == "__main__":
    inputData = readInput()
    finalValue = logicUnit(inputData)
    printData(finalValue)
