from copy import deepcopy
import numpy as np
import MatrixTools as  Mtool
import random

class antSystem:
    def __init__(self,nbAnts,rho,alpha,beta,Q,c,NCmax):
        self.m = nbAnts
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.c = c
        self.NCmax = NCmax

        self.ants = []
        
        for i in range(self.m - 1):
            self.ants.append([0,i+1])
        
        self.pheromoneArray = np.ones((self.m,self.m),dtype=float) * self.c

        self.deltaPheromoneArray = np.zeros((self.m,self.m), dtype=float)


    def addNewNodeToAntsPath(self,matrixIncidence):
        for ant in self.ants:
            fullNodeList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
            noYetBrowsingNodes = list(set(fullNodeList) - set(ant))
            nextNode = Mtool.NextBrowsingNode(self, ant[len(ant) - 1], noYetBrowsingNodes,matrixIncidence)
            ant.append(nextNode)
                

    def getPheromoneArray(self):
        return self.pheromoneArray
    def resetAnts(self):
        self.ants = []
        for i in range(self.m):
            self.ants.append([0,random.randint(1,self.m - 1)])

    def getDeltaPheromoneArray(self):
        return self.deltaPheromoneArray

    def getAnts(self):
        return self.ants

    def getpheromoneArray(self):
        return self.pheromoneArray

    def resetDeltaPheromoneArray(self):
        self.deltaPheromoneArray = np.zeros((self.m,self.m), dtype=float)

    def updateGlobalPheromoneArray(self):
        self.pheromoneArray = np.add(self.pheromoneArray*self.rho,self.deltaPheromoneArray)
        
    def returnOPtimizeSolution(self,matrixIncidence):
        OptimizeSolution = [0]
        
        for i in range(self.m):
            maxPheromone = np.max(self.pheromoneArray[OptimizeSolution[-1]])
            Array = list(self.pheromoneArray[OptimizeSolution[-1]])
            OptimizeSolution.append(Array.index(maxPheromone)) 
        
        #OptimizeSolution = Mtool.goodChild(OptimizeSolution)
        OptimizeSolution.append(0)
        print(OptimizeSolution)
        print(Mtool.pathCost(OptimizeSolution,matrixIncidence)) 
        

                
                

    def addEndingNode(self):
        for ant in self.ants:
            ant.append(ant[0])

    def updateDeltaPheromone(self,matrixIncidence):
        for ant in self.ants:
            pathLength = Mtool.pathCost(ant,matrixIncidence)
            for i in range(self.m - 2):
                self.deltaPheromoneArray[ant[i]][ant[i+1]] = self.deltaPheromoneArray[ant[i]][ant[i+1]] + (self.Q / pathLength)
                
        
    def getNumberOfAnts(self):
        return self.m

    def getEvaporationCoefficient(self):
        return self.p

    def getAlpha(self):
        return self.alpha

    def getBeta(self):
        return self.beta

    def getQ(self):
        return self.Q

    def getc(self):
        return self.c
    
    def getNCmax(self):
        return self.NCmax
