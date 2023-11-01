import pandas as pd
import numpy as numpy
 
TrainSet = pd.read_csv("trainSet.csv")

def IsNearPure(Data):
    PurenessThreshold = 0.9

    _ ,counts = numpy.unique(Data[:,-1],return_counts=True)

    pureness = counts[0]/sum(counts)
   
    return  pureness > PurenessThreshold

def GetPossibleSplits(Data):

    classes,counts = numpy.unique(Data[:,2],return_counts=True)

    # Classification data
    
        

    # Numerical data


    #mostfrequent = classes[numpy.argmax(counts)]
    


    return 
      
def CalculateEntropy():
    return

def FindLowestEntropy():
    return

def Split(Data):



    return

