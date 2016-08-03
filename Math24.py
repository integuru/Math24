from random import randint
from os import remove, rename
import re

#operatorDict = {1:"+", 2:"-", 3:"*", 4:"/"}
#operatorList=[''] * 3
#operandList=[1..10] # define valid card value
#lastCard = 14   # define largest card value; counting J=11, Q=12, K=13
lastCard = 11   # define largest card value; counting J=10, Q=10, K=10
operatorList= ["+", "-", "*", "/"]  # define valid card operators
mathCoolDB = "mathCool24.txt"   # where all values are kept in a file
math24List=[]
math24Dict={}
operations = ['    {:>3} {:>2}   {:>3}   {:>2}   {:>3}     {:>2} {:>3}  ',\
              '  ( {:>3} {:>2}   {:>3} ) {:>2}   {:>3}     {:>2} {:>3}  ',\
              '  ( {:>3} {:>2}   {:>3}   {:>2}   {:>3} )   {:>2} {:>3}  ',\
              '( ( {:>3} {:>2}   {:>3} ) {:>2}   {:>3} )   {:>2} {:>3}  ',\
              '  ( {:>3} {:>2}   {:>3} ) {:>2} ( {:>3}     {:>2} {:>3} )',\
              '    {:>3} {:>2} ( {:>3}   {:>2}   {:>3} )   {:>2} {:>3}  ',\
              '  ( {:>3} {:>2} ( {:>3}   {:>2}   {:>3} ) ) {:>2} {:>3}  ',\
              '    {:>3} {:>2} ( {:>3}   {:>2}   {:>3}     {:>2} {:>3} )',\
              '    {:>3} {:>2}   {:>3}   {:>2} ( {:>3}     {:>2} {:>3} )',\
              '    {:>3} {:>2} ( {:>3}   {:>2} ( {:>3}     {:>2} {:>3} )']

""" with open(mathCoolDB, "r") as mathCool24:
    for line in mathCoolDB:
        mathCoolDict[line] = 1
try:    
    mathCool24=open(mathCoolDB, "r")
    for line in mathCool24:
        math24List.append(line)
    mathCool24.close()
except:
    print(mathCoolDB, " is empty.")
    mathCool24 = open(mathCoolDB,"w")
    mathCool24.close()
"""
#mathCool24=open(mathCoolDB, "w")

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

                            for precedence in operations:
                                questionString = precedence.format(str(a),op1,str(b),op2,str(c),op3,str(d))
                                try:    # in case evaluation fails for division-by-zero, etc.  Skip errors
                                    answer = float(eval(questionString))
                                    if ( answer == 24 ):
                                        #math24List.append(questionString)
                                        #print(questionString)
                                        
                                        temp1=re.sub('^\s+','',questionString)
                                        temp2=re.sub('\s+$','',temp1)
                                        temp1=re.sub('\s+',',',temp2)
                                        temp2=re.split(',',temp1)
                                        temp2.sort()
                                        key = ",".join(temp2)
                                                                                
                                        if key not in list(math24Dict.keys()):
                                            math24Dict[key] = questionString
                                            #print(questionString, '------8<------>8------', key)
                                            #mathCool24.write(questionString + '\n')
                                        break
                                except:
                                    continue
mathCool24=open(mathCoolDB, "w")                                       
for line in sorted(math24Dict.values()):
    mathCool24.write(line + '\n')
mathCool24.close()

