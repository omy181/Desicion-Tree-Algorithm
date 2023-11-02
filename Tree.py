from DataManager import *

def CreateTree(Data):

    ispure,label = IsNearPure(Data)

    if ispure:
        print(label)
        return

    possiblesplits = GetPossibleSplits(Data)

    LowestEntropyAbove,LowestEntropyBellow,Split_Column,Split_Value = FindLowestEntropySplit(Data,possiblesplits)


    classes = numpy.unique(Data[:,Split_Column])
    
    Condition = ""

    if isinstance(classes[0],str):
        # for Categorical
        Condition = "!= ",Split_Value

    else:
        # for Numerical
        Condition = "<= ", classes[Split_Value]

    print(Condition)

    CreateTree(LowestEntropyAbove)
    CreateTree(LowestEntropyBellow)

    return