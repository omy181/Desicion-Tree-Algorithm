from DataManager import *
from Tree import *
import math as math

def CreateForest(TrainData,TestData,RemoveDataCollection,PurenessThreshold,DepthLimit,Positive):

    TP = 0
    TN = 0
    FP = 0
    FN = 0


    # Create Trees
    Trees = []
    for datatoremove in RemoveDataCollection:
        NewData = RemoveData(TrainData,datatoremove)
        tree = CreateTree(numpy.array(NewData),NewData,PurenessThreshold,DepthLimit)
        Trees.append(tree)


    # Ask Questions
    for question in range(len(TestData)):
        Answers = []
        Truth = TestData.iloc[question][-1]
        for tree in Trees:
            Answers.append(AskQuestion(tree,TestData.iloc[question]))       
        
        Prediction = max(set(Answers),key=Answers.count) # most frequent

        if Prediction == Positive:
            if Prediction == Truth:
                TP += 1
            else:
                FP += 1
        else:
            if Prediction == Truth:
                TN += 1
            else:
                FN += 1

    
    return TP,TN,FP,FN


# Creates different sets of parameters for the use of different trees
def CreateRandomForestSet(Data,Count,SetSize):

    Collection = (Data.iloc[:,:-1]).columns

    NewCollection = []

    for i in range(Count):
        NewCollection.append([])

        j = math.floor(i/Count)

        for k in range(j+SetSize):
            NewCollection[i%Count].append(Collection[(i%len(Collection) + k)%len(Collection)])

    return NewCollection