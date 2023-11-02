from DataManager import *
from Tree import *

tree = CreateTree()

TrainData = numpy.array(TrainSet)
    
print(CalculateEntropy(TrainData))





#print(Split(TrainData,1,48.25)) numerical 1st column element 48.25

#print(Split(TrainData,0,0)) cathegorical 0th column and 0th element(a)


#mostfrequent = classes[numpy.argmax(counts)]