from random import randint
from os import remove, rename

#operatorDict = {1:"+", 2:"-", 3:"*", 4:"/"}
#operandList=[0] * 4
operatorList= ["+", "-", "*", "/"]
#operatorList=[''] * 3
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
lastCard=11

for a in range(1,lastCard):
    for b in range(1,lastCard):
        for c in range(1,lastCard):
            for d in range(1,lastCard):
                for i in range(len(operatorList)):
                    op1 = operatorList[i]
                    for j in range(len(operatorList)):
                        op2 = operatorList[j]
                        for k in range(len(operatorList)):
                            op3 = operatorList[k]
                    
                            questionString = str(a) + op1 + \
                                             str(b) + op2 + \
                                             str(c) + op3 + \
                                             str(d)
                                             
                            #print(questionString)
                            answer = float(eval(questionString))
                            if ( answer == int(answer)) and ( int(answer) == 24):
                                print(questionString)
                                math24List.append(questionString)

mathCool24=open(mathCoolDB, "a")
for idx in range(lastCount, len(math24List)):
    #print(math24List[idx])
    line = math24List[idx] + '\n'
    mathCool24.write(line)
mathCool24.close()
