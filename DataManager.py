import pandas as pd
import numpy as numpy
 
TrainSet = pd.read_csv("trainSet.csv")

def IsNearPure(Data):
    PurenessThreshold = 0.9

    _ ,counts = numpy.unique(Data[:,-1],return_counts=True)

    pureness = counts[0]/sum(counts)
   
    return  pureness > PurenessThreshold

def GetPossibleSplits(Data):

    split_columns = {}

    for column in range( (len(TrainSet.columns)-1)):
        classes = numpy.unique(Data[:,column])

        if isinstance(classes[0],str):
            # Classification data
            split_columns[column] = classes        
            
        else:
            # Numerical data
            mean_classes = []
            for i in range(len(classes)-1):
                mean_classes.append((classes[i] + classes[i+1])/2)
              
            split_columns[column] = mean_classes
    
    return split_columns
      
def CalculateEntropy(Data):
    _,Counts = numpy.unique(Data[:,-1],return_counts=True)

    p = Counts/ Counts.sum()
    
    return sum(p * (-numpy.log2(p)))

def FindLowestEntropy():
    return

def Split(Data,Split_Column,Split_Value):

    classes = numpy.unique(Data[:,Split_Column])

    column_values = Data[:,Split_Column]


    if isinstance(classes[0],str):
        # for Categorical
        above = TrainSet[classes[Split_Value] == column_values]
        bellow = TrainSet[classes[Split_Value] != column_values]

    else:
        # for Numerical
        above = TrainSet[Split_Value >= column_values]
        bellow = TrainSet[Split_Value < column_values]    

    return above,bellow

