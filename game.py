import random
l=["rock","paper","sessior"]
'''
rock vs paper --> paper wins
paper vs sessior --> sessior wins
rock vs sessior --> rock wins

'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
GAME START....
                 1.yes
                 2. no|exit
'''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
                                
                                1.rock
                                2.sessior
                                3.paper
'''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="sessior"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            print(uchoice)
            print(Cchoice)

            if Cchoice==uchoice:
                print("computer value:-",Cchoice)
                print("user value:-",uchoice)
                print("GAME DRAW")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="sessior") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="sessior" and Cchoice=="paper"):
                print("computer value:-",Cchoice)
                print("user value:-",uchoice)
                print("YOU WIN")
                ucount=ucount+1
            else:
                print("computer value:-",Cchoice)
                print("user value:-",uchoice)
                ccount=ccount+1
                print("COMPUTER WINS")
        if ucount==ccount:
            print("Final game draw....!")
            print("user score:-",ucount)
            print("computer score:-",ccount)

        elif ucount>ccount:
            print("You wins....")
            print("user score:-",ucount)
            print("computer score:-",ccount)
        
        else:
            print("computer wins...")
            print("user score:-",ucount)
            print("computer score:-",ccount)



                  




            
    else:
        break