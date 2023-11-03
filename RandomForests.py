from DataManager import *
from Tree import *


def CreateForest(TrainData,TestData,RemoveDataCollection,PurenessThreshold,DepthLimit,Positive):

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    # for every question tree is constructed again and again
    # question loop should be inside tree loop

    for question in range(len(TestData)):
        print("Question",question,"/",len(TestData))

        Answers = []
        Truth = TestData.iloc[question][-1]
        for datatoremove in RemoveDataCollection:
            NewData = RemoveData(TrainData,datatoremove)
            tree = CreateTree(numpy.array(NewData),NewData,PurenessThreshold,DepthLimit)
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
