balls=60
player1=int(input("Runs scored by Player 1: "))
player2=int(input("Runs scored by Player 2: "))
player3=int(input("Runs scored by Player 3: "))
sr1=(player1/balls)*100
sr2=(player2/balls)*100
sr3=(player3/balls)*100
print("----------OUTPUT----------")
print("Strike Rate of 1st Player:",sr1)
print("Strike Rate of 2nd Player:",sr2)
print("Strike Rate of 3rd Player:",sr3)
print("Runs Score by 1st Player in Another 60 Balls:",player1*2)
print("Runs Score by 2nd Player in Another 60 Balls:",player2*2)
print("Runs Score by 3rd Player in Another 60 Balls:",player3*2)
print("Maximum Number of Sixes by 1st Player:",player1//6)
print("Maximum Number of Sixes by 2nd Player:",player2//6)
print("Maximum Number of Sixes by 3rd Player:",player3//6)
