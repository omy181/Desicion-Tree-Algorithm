from DataManager import *
from Tree import *
    
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