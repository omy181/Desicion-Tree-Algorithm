from DataManager import *
from Tree import *
from RandomForests import *
from pprint import *


PositiveLabel = "good"

#                                                                       Single Tree
print("\nSingle Tree Results:")

# Parameters = Training set, Training set, Purity treshold, Tree length limit
tree = CreateTree(numpy.array(TrainSet),TrainSet,0.8,6)

print("\nTrain Results:")
# Parameters = Tree, Question set, Label of Positive data
TP,TN,FP,FN = AskQuestionToAll(tree,TrainSet,PositiveLabel)
ShowStatistics(TP,TN,FP,FN)

print("\nTest Results:")
# Parameters = Tree, Question set, Label of Positive data
TP,TN,FP,FN = AskQuestionToAll(tree,TestSet,PositiveLabel)
ShowStatistics(TP,TN,FP,FN)

print("\nPlease Wait...\n")






#                                                                       Random Forest
# Parameters = Training set, Tree Count
RandomForestSet = CreateRandomForestSet(TrainSet,20)

# Parameters = Training set, Test set, Random Forest set, Purity treshold, Tree length limit, Label of Positive data
TP,TN,FP,FN = CreateForest(TrainSet,TestSet,RandomForestSet,0.9,15,PositiveLabel)

print("\nRandom Forest Results:")

print("\nTest Results:")
ShowStatistics(TP,TN,FP,FN)






# For asking single question
# Parameters = Tree, Question Row
#print(AskQuestion(tree,TestSet.iloc[0]))

