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

#Node visibility
def nodeVisibility(startingNode,endingNode,MatrixIncidence):
    return 1 / MatrixIncidence[startingNode][endingNode]
    
#Function to  find the probability of browsing differents Nodes and return the one with the best probability
def NextBrowsingNode(antSystem,currentNode,noYetBrowsingNodes,MatrixIncidence):
    NodeAndProbability = []
    Weigths = [ (math.floor(antSystem.pheromoneArray[currentNode][Node])**antSystem.alpha) * (nodeVisibility(currentNode,Node,MatrixIncidence)**antSystem.beta)  for Node in noYetBrowsingNodes]
    globalWeigth = sum(Weigths)

    for i in range(len(Weigths)):
        NodeAndProbability.append((Weigths[i]/globalWeigth,noYetBrowsingNodes[i]))
    NodeAndProbability.sort(key = lambda x:x[0])
    return NodeAndProbability[-1][1]

#Function to calculate the weight of a path
def pathCost(path,MatrixIncidence):
    weightPath = 0

    for element in range(len(path) - 1) :
        weightPath += MatrixIncidence[path[element]][path[element + 1]]
    
    return weightPath
    

