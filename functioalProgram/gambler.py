#simulate a gambler who start with stake and play until gambler has won or lost
import random

stakeAmount=int(input("Enter stake amount : " ))
goalAmount=int(input("Enter goal amount : " ))
betAmount=int(input("Enter bet amount : " ))
numberOfTimes=int(input("Enter number of times you want to play : " ))
winCount=0
lossCount=0

for index in range(1,numberOfTimes+1,1):
    randomWin=random.randint(0,1)
    if randomWin == 0:
        stakeAmount-=betAmount
        lossCount+=1
    else:
        stakeAmount+=betAmount
        winCount+=1

winPercentage=winCount*100/numberOfTimes
lossPercentage=lossCount*100/numberOfTimes

print(f"win percentage is : {winPercentage}")
print(f"loss percentage is : {lossPercentage}")