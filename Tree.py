import pandas as pd
import math as math

TrainSet = pd.read_csv("trainSet.csv")

class Attr():
   name = ""
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
    print("Count", DataElement.good + DataElement.bad) 
    print("Good", DataElement.good) 
    print("Bad", DataElement.bad) 


def ExtractData(Dict,Column,NumericDivision):
    if type(TrainSet.loc[1][Column]) == str:

        #For Categorical Data
        for i in range(0,len(TrainSet)):
            data = TrainSet.loc[i][Column]

            if not isInList(Dict,data):     
                at = Attr()
                at.name = data
                Dict[at.name] = at
            
            if TrainSet.loc[i][9] == "good":
                Dict[data].good += 1
            else:
                Dict[data].bad += 1
    else:
        #For Numeric Data
        TrainSet.sort_values("A2",axis=0,ascending=True,inplace=True)
        
        Div = int(len(TrainSet)/(NumericDivision + 1))
        DivCount = 1

        for j in range(0,NumericDivision):
            # Smaller than
            at = Attr()
            at.name = "<= " +str(TrainSet.loc[Div*DivCount][Column] )      
            for i in range(0,Div*DivCount):            
                if TrainSet.loc[i][9] == "good":
                    at.good += 1
                else:
                    at.bad += 1   

            Dict[at.name] = at    

            # Bigger than
            at = Attr()
            at.name = "> " +str(TrainSet.loc[Div*DivCount][Column] )      
            for i in range(Div*DivCount,len(TrainSet)):            
                if TrainSet.loc[i][9] == "good":
                    at.good += 1
                else:
                    at.bad += 1   

            Dict[at.name] = at    

            DivCount+=1

       
        

def Entropy(attr:Attr):
        
        if attr.bad == 0 or attr.good == 0: # entropy should be 0
            print("\n",attr.name,"has some 0 attributes")
            return 0   

        pgood = attr.good/(attr.good+attr.bad)
        pbad = attr.bad/(attr.good+attr.bad)
        e = -pgood*math.log2(pgood) - pbad*math.log2(pbad)
        #print("Entropy of ",attr.name,"is ",e)
        return e


def InformationGain(Dict):
    
    TotalAttr = Attr()     
    TotalAttr.name = "Total Attribute"

    for attr in Dict.values():        
        TotalAttr.good += attr.good
        TotalAttr.bad += attr.bad
    
    InfoGain = Entropy(TotalAttr)

    for attr in Dict.values():
        e = Entropy(attr)       
        
        InfoGain += -((attr.good+attr.bad)/(TotalAttr.good+TotalAttr.bad))*e   

    return InfoGain

#                       TESTING
    
A1 = {}
NumericDivisionCount = 2
ExtractData(A1,1,NumericDivisionCount)


for a in A1.keys():
    print("\n")  
    PrintData(A1[a]) 
     
print("\nInfoGain is ",InformationGain(A1))   


"""
PrintData(A1["a"])

PrintData(A1["b"])
"""


