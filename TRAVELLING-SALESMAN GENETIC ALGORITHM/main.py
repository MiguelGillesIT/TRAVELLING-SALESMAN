import MatrixTools as  Mtool
import random
import numpy as np

if __name__ == "__main__":
     
    matrixIncidence = Mtool.fillIncidenceMatrix()
    startingNode = random.randint(0,41)
    Population = []
    
    minimumCostneighbourPath = Mtool.createPathByStartingNode(startingNode)
    minimumCost = Mtool.pathCost2(minimumCostneighbourPath,matrixIncidence)
    print(minimumCostneighbourPath)
    print(minimumCost)
    print()

    for i in range((1000)): 
        for i in range(40):
            neighbourPath = Mtool.findNeighbor2(minimumCostneighbourPath,i)
            neighborPathCost = Mtool.pathCost2(neighbourPath,matrixIncidence)

            if minimumCost > neighborPathCost :
                Population.append(neighbourPath)
                minimumCostneighbourPath = neighbourPath
                

    Population = Mtool.bestElementOfPopulation(Population)

    for k in range(1000):
        Children = Mtool.geneticCrossingAndMutation(Population)
        Population.extend(Children)
        Population = Mtool.bestElementOfPopulation(Population)

    for element in Population:
            print("{} ---> {}".format(element,Mtool.pathCost2(element,matrixIncidence)))
        

    
    
