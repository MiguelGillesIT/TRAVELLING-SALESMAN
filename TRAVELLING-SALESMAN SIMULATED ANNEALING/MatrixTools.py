import numpy as np
import copy
import random
import math


#Function to make incidenceMatrix
def fillIncidenceMatrix():

    #Open and read the file containing edges weights 
    file = open("Matrix.txt", "r")
    matrixElement = file.read()

    #Split the file into single integer for weights of the diagonal matrix
    matrixElement = list(map(int,matrixElement.split(",")))
    matrixIncidence = [[]]
    nbZero = 0

    #For each zero meet, create a new line containing the weight for this line
    for number in matrixElement:
        matrixIncidence[nbZero].append(number)

        if number == 0:
            nbZero += 1
            matrixIncidence.append([])

    #Remove the last line which is useless
    else :
        matrixIncidence.pop(len(matrixIncidence) - 1)

    
    #Reverse the diagonal matrix to form a complete matrix
    for i in range(len(matrixIncidence)) :
        for j in range(i , len(matrixIncidence)) :
            matrixIncidence[i].append(matrixIncidence[j][i])

        #Remove redundant zero on the current line
        matrixIncidence[i].remove(0)

    #Close the file
    file.close()
    return np.array(matrixIncidence)

#Function to  create path by fixing starting node
def createPathByStartingNode(node) :
    #Generate array of 42 value starting from 0 to 41
    path = [element for element in range(42)]

    #Remove the node passing in parameter and shuffle array
    path.remove(node)
    np.random.shuffle(path)

    #Insert the node at the beginning and the end of the array
    path.insert(0,node)
    path.append(node)
    path = np.array(path)

    return path



#Function to return weight on edge in incidenceMatrix
def weightOnEdge(lineNode,ColumnNode,incidenceMatrix) :
    return incidenceMatrix[lineNode][ColumnNode]

#Function to generate a neighbor
def findNeighbor(path,partNumber):

    newPath = list(copy.deepcopy(path[ 1 : (len(path) - 1) ]))
    firstNode = path[0] 

    newPath = np.array_split(newPath, partNumber)
    partShuffle = random.randint(0,partNumber - 1)
    
    np.random.shuffle(newPath[partShuffle])

    newPath = list(np.concatenate(newPath))

    
    newPath.insert(0,firstNode)
    newPath.append(firstNode)

    return np.array(newPath)

#Function to calculate the weight of a path
def pathCost(path,MatrixIncidence):
    weightPath = 0

    for element in range(len(path) - 1) :
        weightPath += MatrixIncidence[path[element]][path[element + 1]]

    return weightPath
    
def neighbourFirst(path):
    neighbours = []
    for i in range(2,len(path) - 1):
        TestPath = copy.deepcopy(path)
        temp = TestPath[1]
        TestPath[1] = TestPath[i]
        TestPath[i] = temp
        neighbours.append(TestPath)
    
    return neighbours

#Function to calculate the probability for a system to be in a state
def stateProbability(pathcost1, pathCost2, Temperature):
    return math.exp((pathcost1 - pathCost2) / Temperature)