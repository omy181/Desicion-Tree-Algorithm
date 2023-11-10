from DataManager import *
from Tree import *
from RandomForests import *
from pprint import *
from Visualisation import VisualiseTree


#                                                    Description
# This Desicion tree algorithm uses C4.5
# It looks at the data and finds all possible splits
# then calculates the entropies of all those splits
# finds the lowest entropy split and splits the data from there
# and until all the slices are near pure this procedure is repeated recursively

# Random forest algorithm is made with Random Subspace Method
# It first creates random sets of parameters
# and create trees using only these parameters
# finally asks same questions to all trees
# and outputs the answers which are on majority




PositiveLabel = "good"

#                                                                       Single Tree
print("\nSingle Tree Results:")

# Parameters = Training set, Training set, Purity treshold, Tree length limit
tree = CreateTree(numpy.array(TrainSet),TrainSet,0.85,6)

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
# Parameters = Training set, Tree Count, Set Size
RandomForestSet = CreateRandomForestSet(TrainSet,20,3)

# Parameters = Training set, Test set, Random Forest set, Purity treshold, Tree length limit, Label of Positive data
TP,TN,FP,FN = CreateForest(TrainSet,TestSet,RandomForestSet,0.8,8,PositiveLabel)

print("\nRandom Forest Results:")

print("\nTest Results:")
ShowStatistics(TP,TN,FP,FN)


VisualiseTree(tree)


# For asking single question
# Parameters = Tree, Question Row
#print(AskQuestion(tree,TestSet.iloc[0]))

