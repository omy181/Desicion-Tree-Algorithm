from DataManager import *
from Tree import *
from pprint import *



tree = CreateTree(numpy.array(TrainSet),0.7,0)

if isinstance(tree,str):
    print("\nImpurity is too low!\n")
else:    


    print("\nTrain Results:")
    AskQuestionToAll(tree,TrainSet,"good")

    print("\nTest Results:")
    AskQuestionToAll(tree,TestSet,"good")



    #print(AskQuestion(tree,TestSet.iloc[0]))
    #pprint(tree)
