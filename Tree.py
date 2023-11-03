from DataManager import *

def CreateTree(Data,WholeData,PurenessThreshold,DepthLimit,Depth = 0):

    ispure,label = IsNearPure(Data,PurenessThreshold)

    if ispure or (DepthLimit != 0 and Depth >= DepthLimit):      
        if Depth == 0:           
            print("\n\n\nImpurity is too low!\n\n\n") 
        return label

    possiblesplits = GetPossibleSplits(Data)

    LowestEntropyAbove,LowestEntropyBellow,Split_Column,Split_Value = FindLowestEntropySplit(Data,possiblesplits)


    classes = numpy.unique(Data[:,Split_Column])

    

    Condition = ""

    if isinstance(classes[0],str):
        # for Categorical
        Condition = WholeData.columns[Split_Column] + " != " + classes[Split_Value]

    else:
        # for Numerical
        Condition = WholeData.columns[Split_Column] + " <= " + str(Split_Value)
        
    Tree_Structure = {Condition:[]}
    
    yes_answer = CreateTree(LowestEntropyAbove,WholeData,PurenessThreshold,DepthLimit,Depth+1)
    no_answer = CreateTree(LowestEntropyBellow,WholeData,PurenessThreshold,DepthLimit,Depth+1)

    Tree_Structure[Condition].append(yes_answer)
    Tree_Structure[Condition].append(no_answer)

    return Tree_Structure

def AskQuestion(Tree_Structure,QuestionData):

    question = list(Tree_Structure.keys())[0]

    while True:
        attribute,operator,value = question.split()

        if operator == "<=": # numerical
            if QuestionData[attribute] <= float(value):
                answer = Tree_Structure[question][0]  # yes
            else:
                answer = Tree_Structure[question][1]  # no
        else: # categorical
            if QuestionData[attribute] == value:
                answer = Tree_Structure[question][0]  # yes
            else:
                answer = Tree_Structure[question][1]  # no
        

        if isinstance(answer,str):
            #Answer found
            return answer
        else:      
            #Answer not found
            Tree_Structure = answer
            question = list(answer.keys())[0]



    return

# "Positive" is the desired prediction string, in this case it's "good"
def AskQuestionToAll(Tree_Structure,Data,Positive):

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for question in range(len(Data)):
        Prediction = AskQuestion(Tree_Structure,Data.iloc[question])
        Truth = Data.iloc[question][-1]

        if Prediction == Positive:
            if Prediction == Truth:
                TP += 1
            else:
                FP += 1
        else :
            if Prediction == Truth:
                TN += 1
            else:
                FN += 1


    return TP,TN,FP,FN


def ShowStatistics(TP,TN,FP,FN):

        Accuracy = (TP+TN)/(FP+FN+TP+TN)
        TPrate = TP/(TP+FN)
        FPrate = FP/(TP+FN)
        Presicion = TP/(FP+TP)
        FScore = 2*(Presicion*TPrate)/(Presicion+TPrate)

        print("Accuracy: ",Accuracy)
        print("TPrate: ",TPrate)
        print("FPrate: ",FPrate)
        print("Presicion: ",Presicion)
        print("FScore: ",FScore)
        print("Total number of TP: ",TP)
        print("Total number of TN:: ",TN)
        print("Total number of FP: ",FP)
        print("Total number of FN:: ",FN)

        return