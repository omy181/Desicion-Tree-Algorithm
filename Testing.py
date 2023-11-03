from DataManager import *
from Tree import *
from RandomForests import *
from pprint import *


#tree = CreateTree(numpy.array(TrainSet),TrainSet,0.7,0)



#RemoveDataCollection= [["A1"],["A2"],["A3","A4"],["A4","A6","A8"],["A5"],["A6"],["A7"],["A8"],["A9"]]
RemoveDataCollection= [["A1"],["A2"]]
TP,TN,FP,FN = CreateForest(TrainSet,TrainSet,RemoveDataCollection,0.7,1,"good")
ShowStatistics(TP,TN,FP,FN)

"""
print("\nTrain Results:")
TP,TN,FP,FN = AskQuestionToAll(tree,TrainSet,"good")
ShowStatistics(TP,TN,FP,FN)

print("\nTest Results:")
TP,TN,FP,FN = AskQuestionToAll(tree,TestSet,"good")
ShowStatistics(TP,TN,FP,FN)
"""


#print(AskQuestion(tree,TestSet.iloc[0]))
#pprint(tree)
