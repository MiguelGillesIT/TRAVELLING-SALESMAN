import MatrixTools as  Mtool
import random

if __name__ == "__main__":
     

    matrixIncidence = Mtool.fillIncidenceMatrix()
    startingNode = random.randint(0,41)

    path = Mtool.createPathByStartingNode(startingNode)
    pathCost = Mtool.pathCost(path,matrixIncidence)

    minimumCost = pathCost
    minimumCostneighbourPath = path
    
    print("{} -->  {}".format(list(path),pathCost))
    nbMinimum = 0

    for i in range((100000)): 
        for neighborPath in Mtool.neighbourFirst(path):
            neighborPathCost = Mtool.pathCost(neighborPath,matrixIncidence)

            if minimumCost > neighborPathCost :
                minimumCostneighbourPath = neighborPath
                minimumCost = neighborPathCost
                nbMinimum += 1
                print("")
                print("{}. {} -->  {}".format(nbMinimum,list(minimumCostneighbourPath),minimumCost))
        
        path = minimumCostneighbourPath
        
                
    