import random
import time

def randomRestart():
    columnList = [0] * 8
    for i in range(8):
        columnList[i] = random.randint(1, 8)
    return columnList


# shows queens position on the board
def printBoard(columnList):
    for i in range(8, 0, -1):
        for j in range(8):
            if columnList[j] == i:
                print("X", end="  ")
            else:
                print(0, end="  ")
        print()


def captureNum(columnList):
    captureCounter = 0
    for i in range(0, len(columnList) - 1):
        for j in range(i + 1, len(columnList)):
            if columnList[i] == columnList[j]:
                captureCounter += 1
            if (columnList[i] - columnList[j]) == i - j or (columnList[i] - columnList[j]) == -(i - j):
                captureCounter += 1
    return captureCounter


# shows board status to see attacking queens number for every square
def printBoardAttackingNum(captures):
    print("chess board state that shows number of queens that will attacking each other")
    print("--------------------------")
    for i in range(7, -1, -1):
        print("|", end="")
        for j in range(8):
            print('{:3}'.format(captures[j][i]), end="")
        print("|", end="")
        print()
    print("--------------------------")


def findCaptures(columnList):
    captureList = [[0 for i in range(8)] for i in
                   range(8)]  # taşların olası yerlerindeki karşılatırmaların atılacağı liste
    for m in range(8):
        # to find smallest number of attacking queens number for next iteration, every location is tried therefore initial locations are kept
        copyColumnList = columnList.copy()
        for n in range(8):
            if columnList[m] == n + 1:  # if queens are where they were before
                captureList[m][n] = captureNum(columnList)
                continue
            elif copyColumnList[m] != n + 1:
                copyColumnList[m] = n + 1
                captureList[m][n] = captureNum(copyColumnList)
    return captureList


randomRestartList = []
relocationList = []
timeList = []

for problemCounter in range(25):
    print("SOLUTION #{}".format(problemCounter + 1))
    #queensPositions = [0] * 8
    queensPositions = randomRestart()
    print("queens positions on the column : ", queensPositions)  # tahtadaki taşların konumları
    # board start position
    print("Queens' initial position:")
    printBoard(queensPositions)
    print("-----------------------")

    copyQueensPosition = queensPositions.copy()
    # captureNumList = [[0 for i in range(8)] for i in range(8)]  # taşların olası yerlerindeki karşılatırmaların atılacağı liste
    randomRestartCounter = 0  # increase when chess board restart randomly.
    relocationCounter = 0

    startTime = time.time()
    while captureNum(queensPositions) > 0:
        # do, until there is no capture
        relocationCounter += 1
        print("#{} iteration ".format(relocationCounter))
        print("encountered capture: ", captureNum(queensPositions))
        print("queens positions on columns before changing: ", queensPositions)  # tahtadaki taşların konumları

        captureNumList = findCaptures(queensPositions)

        """print("--------------------------------------")
        printBoardAttackingNum(captureNumList)                      # test for capture numbers
        print("--------------------------------------")"""

        smallestCap = captureNum(
            queensPositions)  # assigning initial capture number before finding smallest capture number

        column, row = -1, -1  # indicates the index that has smallest number of attacking queen
        for i in range(8):
            for j in range(8):
                if captureNumList[i][j] < smallestCap:
                    smallestCap = captureNumList[i][j]
                    column, row = i, j
        # print("column, row: ", column, ",", row)
        print("smallest number of queens attacking each other ", smallestCap)
        if column != -1:  # if column or row values changes that means we find next position
            queensPositions[column] = row + 1
            print("queens positions columns after relocation a queen: ",
                  queensPositions)  # tahtadaki taşların konumları
        else:
            # random restart
            print("encountered local optimum, random restarting...")
            queensPositions = randomRestart()
            copyQueensPosition = queensPositions.copy()
            randomRestartCounter += 1
            print("queens' positions columns after random restart: ",
                  queensPositions)  # tahtadaki taşların konumları
            printBoard(queensPositions)

        # print("capture counter: ", captureNum(queensPositions))

        print("--------------------------------------------------------------------------")

    print("################## solution #{}  ################".format(problemCounter + 1))
    print("Final queens positions on columns : ", queensPositions)  # tahtadaki taşların konumları
    printBoard(queensPositions)
    #print("capture counter: ", captureNum(queensPositions))
    print("Number of random restart in solution #{}:".format(problemCounter + 1), randomRestartCounter)

    randomRestartList.append(randomRestartCounter)
    relocationList.append(relocationCounter)
    print()
    print()
    endTime = time.time()
    timeList.append(endTime - startTime)

print()
print("**************** END OF PROGRAM STATICS ***********************")
print("{:<12}{:<12}{:<18}{:<15}".format("", "Relocation", "Random restart", "Time (sec)"))
for i in range(25):
    print("#{:<11}".format((i + 1)), end="")
    print("{:<12}".format(relocationList[i]), end="")
    print("{:<18}".format(randomRestartList[i]), end="")
    print("{:<15.5f}".format(timeList[i]))
print("--------------------------------------------------")
print("{:<12}{:<12}{:<18}".format("Average", sum(relocationList)/25, sum(randomRestartList)/25),end="")
print("{:<15.5f}".format(sum(timeList)/25))
