'Return all the numbers that can be evaluated to 24'

lastCard = 11   # define largest card value; counting J=10, Q=10, K=10
#lastCard = 14   # define largest card value; counting J=11, Q=12, K=13
cardDeck=range(1,lastCard)
operatorList= ["+", "-", "*", "/"]  # define valid card operators
# Add precedence to the operations by placing () around a plain formula
operations = ['    {:>3} {:>2}     {:>3}   {:>2}   {:>3}       {:>2} {:>3}    ',\
              '  ( {:>3} {:>2}     {:>3} ) {:>2}   {:>3}       {:>2} {:>3}    ',\
              '    {:>3} {:>2}   ( {:>3}   {:>2}   {:>3} )     {:>2} {:>3}    ',\
              '    {:>3} {:>2}     {:>3}   {:>2} ( {:>3}       {:>2} {:>3} )  ',\
              '  ( {:>3} {:>2}     {:>3} ) {:>2} ( {:>3}       {:>2} {:>3} )  ',\
              '(   {:>3} {:>2}     {:>3}   {:>2}   {:>3}   )   {:>2} {:>3}    ',\
              '( ( {:>3} {:>2}     {:>3} ) {:>2}   {:>3}   )   {:>2} {:>3}    ',\
              '(   {:>3} {:>2}   ( {:>3}   {:>2}   {:>3} ) )   {:>2} {:>3}    ',\
              '    {:>3} {:>2} (   {:>3}   {:>2}   {:>3}       {:>2} {:>3}   )',\
              '    {:>3} {:>2} ( ( {:>3}   {:>2}   {:>3} )     {:>2} {:>3}   )',\
              '    {:>3} {:>2} (   {:>3}   {:>2} ( {:>3}       {:>2} {:>3} ) )']
              
mathCoolDB = "mathCool24.txt"   # where all values are kept in a file
math24Dict={}

for a in cardDeck:
    for b in cardDeck:
        for c in cardDeck:
            for d in cardDeck:
                for op1 in operatorList:
                    for op2 in operatorList:
                        for op3 in operatorList:
                            
                            for precedence in operations:
                                questionString = precedence.format(str(a),op1,str(b),op2,str(c),op3,str(d))
                                try:    # in case evaluation fails for division-by-zero, etc.  Skip errors
                                    answer = float(eval(questionString))
                                    if ( answer == 24 ):
                                        key = str(sorted([str(a),str(b),str(c),str(d)]))                                       
                                        if key not in list(math24Dict.keys()):
                                            #print(questionString)
                                            math24Dict[key] = questionString
                                        break
                                except:
                                    continue

mathCool24=open(mathCoolDB, "w")                                       
for value in sorted(math24Dict.values()):
    mathCool24.write(value + '\n')
mathCool24.close()

