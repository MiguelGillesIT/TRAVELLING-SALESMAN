import MatrixTools as  Mtool
import random

if __name__ == "__main__":
     
    matrixIncidence = Mtool.fillIncidenceMatrix()
    startingNode = random.randint(0,41)

    path = Mtool.createPathByStartingNode(startingNode)
    pathCost = Mtool.pathCost(path,matrixIncidence)

    minimumPathCost = pathCost
    minimumCostNeighbourPath = path

    t = 1000
    cool = 0.95
    alpha = 0.1
    
    print("{} -->  {}".format(list(path),pathCost))

    while t > alpha :
        
        for neighbourPath in Mtool.neighbourFirst(path):
            neighborPathCost = Mtool.pathCost(neighbourPath,matrixIncidence)
            if minimumPathCost > neighborPathCost :
                        minimumCostNeighbourPath = neighbourPath
                        minimumPathCost = neighborPathCost
                        print("")
                        print(" {} -->  {}".format(list(minimumCostNeighbourPath),minimumPathCost))
        else: 
            path = minimumCostNeighbourPath
        r = random.random()
        if r < Mtool.stateProbability(minimumPathCost,neighborPathCost,t) :
            minimumCostNeighbourPath = neighbourPath
            minimumPathCost = neighborPathCost
            print(" {} -->  {}".format(list(minimumCostNeighbourPath),minimumPathCost))

        t = t * cool