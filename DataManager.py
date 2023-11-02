import pandas as pd
import numpy as numpy
 
TrainSet = pd.read_csv("trainSet.csv")

def IsNearPure(Data):
    PurenessThreshold = 0.9

    classes ,counts = numpy.unique(Data[:,-1],return_counts=True)

    pureness = counts[0]/sum(counts)

    mostfrequent = classes[numpy.argmax(counts)]
   
    return  pureness > PurenessThreshold , mostfrequent

def GetPossibleSplits(Data):

    split_columns = {}

    for column in range( (len(TrainSet.columns)-1)):
        classes = numpy.unique(Data[:,column])

        if isinstance(classes[0],str):
            # Classification data

            arr = []
            for i in range(len(classes)) :
                arr.append(i)

            split_columns[column] = arr
            
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

def FindLowestEntropySplit(Data,split_columns):

    LowestEntropy = CalculateEntropy(Data)
    LowestEntropyAbove = None
    LowestEntropyBellow = None
    Split_Column = 0
    Split_Value = 0

    for i in range(0,len(Data[0])-1):
        for a in split_columns[i]:
            
            above,bellow = Split(Data,i,a)

            e_above = CalculateEntropy(above.to_numpy())
            e_bellow = CalculateEntropy(bellow.to_numpy())

            p_above = len(above)/ (len(above)+len(bellow))
            p_bellow = len(bellow)/ (len(above)+len(bellow))

            e_overall = p_above * e_above + p_bellow * e_bellow

            if e_overall <= LowestEntropy:
                LowestEntropy = e_overall
                LowestEntropyAbove = above
                LowestEntropyBellow = bellow
                Split_Column = i
                Split_Value = a


    return LowestEntropyAbove,LowestEntropyBellow,Split_Column,Split_Value


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

