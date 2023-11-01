from DataManager import *
from Tree import *

tree = CreateTree()

TrainData = numpy.array(TrainSet)
    
print(GetPossibleSplits(TrainData))

