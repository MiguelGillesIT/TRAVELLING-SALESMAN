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
def pathCost(path):
    MatrixIncidence = fillIncidenceMatrix()
    weightPath = 0

    for element in range(len(path) - 1) :
        weightPath += MatrixIncidence[path[element]][path[element + 1]]

    return weightPath

#Function to calculate the weight of a path
def pathCost2(path,MatrixIncidence):
    weightPath = 0

    for element in range(len(path) - 1) :
        weightPath += MatrixIncidence[path[element]][path[element + 1]]

    return weightPath

    

#Function to return three bests elements of the population
def bestElementOfPopulation(kPopulation):
    Paths = list(kPopulation)
    Paths.sort(key = pathCost)
    Paths = Paths[:15]
    return Paths
   
def findNeighbor2(Path,number):
    path = Path[1:len(Path) -1]
    tempPath = list(path)
    temp = tempPath[number]
    tempPath[number] = tempPath[number+1]
    tempPath[number+1] = temp
    tempPath.insert(0,Path[0])
    tempPath.append(Path[0])
        
    return tempPath

#Function to get a goodchild and erase many occurence of a node

def goodChild(child,startingNode):
    #Fill the list of all nodes and remove the first from all node
    fullNodeList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
    fullNodeList.remove(startingNode)

    #Find nodes which are not in child nodes
    missingNodesList = list(set(fullNodeList) - set(child))
    
    #Starting from the middle of the child (new chromosom) verify if an element occur twice and replace 
    #Replace element by the end of missing nodes list
    for i in range(20,41):
        if(child.count(child[i]) == 2):
            child[i] = missingNodesList.pop()

    #Add starting node in the beginning and the ending of child
    child.insert(0,startingNode)
    child.append(startingNode)
    return child

#Function to cross Parents
def geneticCrossingAndMutation(Population):
    Children = []

    for i in range(len(Population)):
        for j in range(len(Population)):
            if( i != j ):
                if(random.random() < 0.6):
                    Child = list(Population[i][1:21]) + list(Population[j][21:42])
                    Child = goodChild(Child,Population[i][0])

                    if(random.random() < 0.2):
                        Child = geneticMutation(Child)

                    if(not((Child == child).all() for child in Population)):
                        Children.append(Child)
                  
    return Children

#Function to do mutation in a child
def geneticMutation(child):
    #Trim the child and reverse the first and last five node on him
    firstChildPart = child[:5]  
    lastChildPart = child[38:]
    child = list(lastChildPart[::-1]) + list(child[5:38]) + list(firstChildPart[::-1])        
    return child
    