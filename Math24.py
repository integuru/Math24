from random import randint
from os import remove, rename

operatorDict = {1:"+", 2:"-", 3:"*", 4:"/"}
operandList=[0] * 4
operatorList=[''] * 3
mathCoolDB = "mathCool24.txt"
maxCount=2000    # Maximum Count for each run
math24List=[]

"""
with open(mathCoolDB, "r") as mathCool24:
    for line in mathCoolDB:
        mathCoolDict[line] = 1
"""

try:    
    mathCool24=open(mathCoolDB, "r")
    
    for line in mathCool24:
        math24List.append(line)
        
    mathCool24.close()
except:
    print(mathCoolDB, " is empty.")
    mathCool24 = open(mathCoolDB,"w")
    mathCool24.close()
    
    
count=0
lastCount=len(math24List)
#maxCount += count

while True:
    for idx in range(len(operandList)):
        operandList[idx]=randint(1,10)
    #print(operandList)
    
    questionString=str(operandList[0])
    for idx in range(len(operatorList)):
        operatorList[idx]=operatorDict[randint(1,len(operatorDict))]
        questionString += operatorList[idx] + str(operandList[idx+1])
    #print(questionString)
    answer = float(eval(questionString))
    if answer < 0:
        continue
    if answer == int(answer):
        #print("Lucky Integer:\t", questionString, "=", int(answer), ".")
        if int(answer) == 24:
            #print("***  Bingo 24: ", questionString, "=", int(answer), "  ***")
            #print(questionString)
            if questionString not in math24List:
                
                math24List.append(questionString)
                count += 1
                if count == maxCount :
                    break
            #break
        
    #else:
        #print("Unlucky floats:\t", questionString, "=", answer, ".")

mathCool24=open(mathCoolDB, "a")
for idx in range(lastCount, len(math24List)):
    print(math24List[idx])
    line = math24List[idx] + '\n'
    mathCool24.write(line)
mathCool24.close()
    
    
