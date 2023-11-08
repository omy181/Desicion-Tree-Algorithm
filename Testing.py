from DataManager import *
from Tree import *
from RandomForests import *
from pprint import *
from Visualisation import VisualiseTree


PositiveLabel = "good"



#                                                                       Single Tree
print("\nSingle Tree Results:")

# Parameters = Training set, Training set, Purity treshold, Tree length limit
tree = CreateTree(numpy.array(TrainSet),TrainSet,0.85,6)

print("\nTrain Results:")
# Parameters = Tree, Question set, Label of Positive data
TP,TN,FP,FN = AskQuestionToAll(tree,TrainSet,PositiveLabel)
ShowStatistics(TP,TN,FP,FN)

"""
print("\nTest Results:")
# Parameters = Tree, Question set, Label of Positive data
TP,TN,FP,FN = AskQuestionToAll(tree,TestSet,PositiveLabel)
ShowStatistics(TP,TN,FP,FN)

print("\nPlease Wait...\n")


#                                                                       Random Forest
# Parameters = Training set, Tree Count, Set Size
RandomForestSet = CreateRandomForestSet(TrainSet,20,3)

# Parameters = Training set, Test set, Random Forest set, Purity treshold, Tree length limit, Label of Positive data
TP,TN,FP,FN = CreateForest(TrainSet,TestSet,RandomForestSet,0.8,8,PositiveLabel)

print("\nRandom Forest Results:")

print("\nTest Results:")
ShowStatistics(TP,TN,FP,FN)

"""

VisualiseTree(tree)

# For asking single question
# Parameters = Tree, Question Row
#print(AskQuestion(tree,TestSet.iloc[0]))

