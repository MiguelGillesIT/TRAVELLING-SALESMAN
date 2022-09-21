import MatrixTools as  Mtool
import antSystemVariable as AS


if __name__ == "__main__":
     
    matrixIncidence = Mtool.fillIncidenceMatrix()

    #Initialize the  Ants System
    AntSystem = AS.antSystem(42,0.5,1,5,100,2,1000)
    for j in range(AntSystem.getNCmax()):
        
        for i in range(AntSystem.getNumberOfAnts() - 2):
            AntSystem.addNewNodeToAntsPath(matrixIncidence)
        AntSystem.addEndingNode()
        
        

        AntSystem.updateDeltaPheromone(matrixIncidence)
        #print("DeltaPheromone After Update")
        #print(AntSystem.getDeltaPheromoneArray())
        #print()

        AntSystem.updateGlobalPheromoneArray()
        #print("PheromoneArray After Update")
        #print(AntSystem.getpheromoneArray())
        #print()

        AntSystem.resetDeltaPheromoneArray()
        #print("Ants After Rest")
        #print(AntSystem.getDeltaPheromoneArray())
        #print()
        
        AntSystem.resetAnts()
        #print("Ants After Update")
        #print(AntSystem.getAnts())
        #print()
    
    
        
    AntSystem.returnOPtimizeSolution(matrixIncidence)
    