from ast import In
import MatrixTools as  Mtool
import random
import numpy as np

if __name__ == "__main__":

    ListTaboo = []
    matrixIncidence = Mtool.fillIncidenceMatrix()
    startingNode = random.randint(0,41)

    InitialPath = Mtool.createPathByStartingNode(startingNode)
    MinimumPathCost = Mtool.pathCost(InitialPath,matrixIncidence)
    rightNeighbouringFunction = 0
    print("Initial Path {}".format(InitialPath))
    print()
    print()
    for k in range((2000)):

        if  rightNeighbouringFunction == 0:
            neighbours = Mtool.neighbourFirst(InitialPath)
        elif rightNeighbouringFunction == 1:
            neighbours = Mtool.neighbourSecond(InitialPath)
        else:
            neighbours = Mtool.neighbourThird(InitialPath)

        for neigbhour in neighbours:
            
            if Mtool.pathCost(neigbhour,matrixIncidence) < MinimumPathCost:
                MinimumPathCost = Mtool.pathCost(neigbhour,matrixIncidence)
                MinimumPath  = neigbhour
                MinimumIndex = neighbours.index(MinimumPath)
                randomIndex = random.randint(0,len(neighbours) - 1)
                while randomIndex == MinimumIndex:
                    randomIndex = random.randint(0,len(neighbours) - 1)
                InitialPath = neighbours[randomIndex]

        if(MinimumPath not in ListTaboo):
            ListTaboo.append(MinimumPath) 
        else:
            if rightNeighbouringFunction == 0:
                print("Changement1")
                rightNeighbouringFunction = 1

            elif rightNeighbouringFunction == 1:
                print("Changement2")
                rightNeighbouringFunction = 2

            else:
                print("Changement3")
                rightNeighbouringFunction = 0

        if(len(ListTaboo) > 50):
            ListTaboo.pop(0)

    for element in ListTaboo :
        print("{} ----> {}".format(element,Mtool.pathCost(element,matrixIncidence)))

    
   

    
        

    
    
