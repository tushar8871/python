#Get number of flips from user
#Genrate random coin side using random and calculate its percentage
import random

numberOfTimes=int(input("Enter number of flip : "))
tries = 0
heads = 0
tails = 0
for tries in range(numberOfTimes):
    coin = random.randint(0,1)
    if coin == 1:
        heads += 1
    else:
        tails += 1

hPercentage=heads*100/numberOfTimes
tPercentage=tails*100/numberOfTimes

print("Heads : ",hPercentage)
print("Tails : ",tPercentage)