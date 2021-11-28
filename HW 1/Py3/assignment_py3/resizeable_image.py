from os import error
import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
        if (dp):
            return self.dpBestSeam()
        else:
            return self.noDPSeam()
    
#i represents width, columns
#j represents height, rows

#Create a energy matrix with all the values calculated, once at the bottom, make way back up to find most optimal path
    def dpBestSeam(self):
        energyMatrix = [[0 for j in range(self.width)] for i in range(self.height)]
        cords = [0 for j in range(self.height)]
        for j in range(self.height):
            for i in range(self.width):
                # make the first row all zeros since next row needs previous row values to determine its values and if it starts at 10,000 then that wouldn't make sense
                if j == 0:
                    energyMatrix[j][i] = 0
                # just get the energy, can't move anywhere back
                elif i == 0 or j == 0:
                    energyMatrix[j][i] = self.energy(i, j)
                # if at the last column just check the other two locations where previous energy matters
                elif i == (self.width -1 ):
                    energyMatrix[j][i] = (min(energyMatrix[j-1][i-1], energyMatrix[j][i-1]) + self.energy(i, j))
                #if not at the last column and at last row then subtract 10,000 from resulted value since self.energy makes all last row items be 10,000
                elif (j == self.height - 1) and (i != self.width - 1):
                    energyMatrix[j][i] = min(energyMatrix[j-1][i-1], energyMatrix[j-1][i], energyMatrix[j - 1][i + 1]) + self.energy(i, j) - 10000
                # check through all adjacent energys if previous statements aren't true
                else:
                    energyMatrix[j][i] = min(energyMatrix[j-1][i-1], energyMatrix[j-1][i], energyMatrix[j - 1][i + 1]) + self.energy(i, j)
        
        #going backwards in energy matrix, get lowest value that is adjacent to recent lowest pixel
        #once gotten store the value then continue with process until all the way back to top
        for j in range(self.height -1 , -1, -1):
            if j == self.height -1:
                cords[j] = [energyMatrix[j].index(min(energyMatrix[j])), j]
            else:
                prevIndex = cords[j+1][0]
                minValue = min(energyMatrix[j][prevIndex + 1], energyMatrix[j][prevIndex - 1], energyMatrix[j][prevIndex])
                if (minValue == energyMatrix[j][prevIndex + 1]):
                    cords[j] = [prevIndex + 1, j]
                elif (minValue == energyMatrix[j][prevIndex - 1]):
                    cords[j] = [prevIndex - 1, j]
                else:
                    cords[j] = [prevIndex, j]
        return cords

    
    def noDPSeam(self):
        lastEnergyValues = [0 for j in range(self.width)] #needs at least the last energy values to compute the new ones
        newEnergyValues = [0 for j in range(self.width)]
        cords = [0 for j in range(self.height)]
        n = self.height
        
        while n != 0: #continiously compute energys up to n, with n intially being the height and slowly lowering down while more cordinates are computed
            for j in range(n):
                for i in range(self.width):
                    if j == 0:
                        newEnergyValues[i] = 0
                    elif i == (self.width - 1):
                        newEnergyValues[i] = min(lastEnergyValues[i-1], lastEnergyValues[i]) + self.energy(i, j)
                    elif (j == self.height - 1) and (i != self.width - 1):
                        newEnergyValues[i] = min(lastEnergyValues[i-1], lastEnergyValues[i], lastEnergyValues[i+1]) + self.energy(i, j) - 10000
                    else:
                        newEnergyValues[i] = min(lastEnergyValues[i-1], lastEnergyValues[i], lastEnergyValues[i+1]) + self.energy(i, j)
                lastEnergyValues.clear()
                lastEnergyValues.extend(newEnergyValues) #make the new energy values now the last energy values
            n -= 1
            if j == self.height -1:
                cords[j] = [newEnergyValues.index(min(newEnergyValues)), j]
            else:
                prevIndex = cords[j+1][0]
                minValue = min(newEnergyValues[prevIndex-1], newEnergyValues[prevIndex], newEnergyValues[prevIndex+1])
                if (minValue == newEnergyValues[prevIndex + 1]):
                    cords[j] = [prevIndex + 1, j]
                elif (minValue == newEnergyValues[prevIndex - 1]):
                    cords[j] = [prevIndex - 1, j]
                else:
                    cords[j] = [prevIndex, j]
        return cords


        

        


