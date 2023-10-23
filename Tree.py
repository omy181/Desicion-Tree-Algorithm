import pandas as pd

TrainSet = pd.read_csv("trainSet.csv")

class Attr():
   name = ""
   count = 0
   good = 0
   bad = 0

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

A1 = {}

column = 0
for i in range(0,len(TrainSet)):
    data = TrainSet.loc[i][column]

    if not isInList(A1,data):     
        at = Attr()
        at.name = data
        A1[at.name] = at
    
    A1[data].count += 1
    if TrainSet.loc[i][9] == "good":
       A1[data].good += 1
    else:
       A1[data].bad += 1
    

for a in A1.keys():
    print("\n")  
    PrintData(A1[a])     



"""
PrintData(A1["a"])

PrintData(A1["b"])
"""


