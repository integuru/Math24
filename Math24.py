from random import randint
from os import remove, rename

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
                                        math24List.append(questionString)
                                        print(questionString)
                                        break
                                        """
                                        temp=[str(a),op1,str(b),op2,str(c),op3,str(d)].extend(precedence)
                                        temp.sort()
                                        key = ",".join(temp)
                                                                                
                                        if key not in list(math24Dict.keys()):
                                            math24Dict[key] = questionString
                                            print(questionString)
                                            """
                                except:
                                    continue
                                        
                                
mathCool24=open(mathCoolDB, "w")
for answer in math24List:
    line = answer + '\n'
    mathCool24.write(line)
mathCool24.close()
