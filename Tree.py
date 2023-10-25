import pandas as pd
import math as math

TrainSet = pd.read_csv("trainSet.csv")

class Attr():
   name = ""
   count = 0
   good = 0
   bad = 0
   entropy = 0

def isInList(list,element):
    state = False
    for i in list.values():
      if element == i.name:
         state = True
         break
    return state


def PrintData(DataElement):
    print("Name", DataElement.name) 
    print("Count", DataElement.count) 
    print("Good", DataElement.good) 
    print("Bad", DataElement.bad) 

def ExtractData(Dict,Column):
    for i in range(0,len(TrainSet)):
        data = TrainSet.loc[i][Column]

        if not isInList(Dict,data):     
            at = Attr()
            at.name = data
            Dict[at.name] = at
        
        Dict[data].count += 1
        if TrainSet.loc[i][9] == "good":
            Dict[data].good += 1
        else:
            Dict[data].bad += 1

def Entropy(attr:Attr):
        
        if attr.bad == 0 or attr.good == 0: # entropy should be 0
            print("\n",attr.name,"has some 0 attributes")
            return 0   

        pgood = attr.good/attr.count
        pbad = attr.bad/attr.count
        e = -pgood*math.log2(pgood) - pbad*math.log2(pbad)
        #print("Entropy of ",attr.name,"is ",e)
        return e


def InformationGain(Dict):
    
    TotalAttr = Attr()     
    TotalAttr.name = "Total Attribute"

    for attr in Dict.values():
        TotalAttr.count+=attr.count
        TotalAttr.good += attr.good
        TotalAttr.bad += attr.bad
    
    InfoGain = Entropy(TotalAttr)

    for attr in Dict.values():
        e = Entropy(attr)       
        
        InfoGain += -(attr.count/TotalAttr.count)*e   

    return InfoGain

#                       TESTING
    
A1 = {}

ExtractData(A1,0)

for a in A1.keys():
    print("\n")  
    PrintData(A1[a]) 
     
print("\nInfoGain is ",InformationGain(A1))   


"""
PrintData(A1["a"])

PrintData(A1["b"])
"""


