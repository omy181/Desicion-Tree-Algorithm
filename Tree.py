from DataManager import *

class TreeNode():
    Attribute:Attr
    Childeren = {}
    NodeEntropy = 0


def CreateTree(trainset:pd.DataFrame):

    NumericDivisionCount = 2
    InfoGains = []

    # Calculate Info Gains
    for i in range(0,len(trainset.columns)-1):
        A1 = {}
        ExtractData(A1,i,NumericDivisionCount)
        InfoGains.append(InformationGain(A1))
    
    LeastInfoGainIndex = FindSmallest(InfoGains)
    
    # Create Node
    RootNode = TreeNode()
    A = {}
    ExtractData(A,LeastInfoGainIndex,NumericDivisionCount)
    RootNode.Attribute = A

    return RootNode


def PrintTree(Treenode:TreeNode):   
    for a in Treenode.Attribute.keys():
        print("\n")  
        #print(Treenode.Attribute[a].name)
        PrintData(Treenode.Attribute[a])  

def FindSmallest(arr):
    smallest = 0
    for i in range(1,len(arr)-1):
        if arr[i] < arr[smallest]:
             smallest = i
    return smallest
    