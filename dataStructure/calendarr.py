#genrate calendar without usong module

#method to generate calendar
def calendar(noOfDays,weekDay):
    #check if weekDay is same or not
    if weekDay=="sun":
        day=0
    elif weekDay=="mon":
        day=1
    elif weekDay=="tue":
        day=2
    elif weekDay=="wed":
        day=3
    elif weekDay=="thu":
        day=4
    elif weekDay=="fri":
        day=5
    elif weekDay=="sat":
        day=6

    #print days
    print("Su Mo Tu We Th Fr Sa")
    #print dates
    for i in range(day):
        print("  ",end=" ")
    i=1
    while (i<=noOfDays):
        #print the dates
        if i<10:
            print("",i,end=" ")
        else:
            print(i,end=" ")
        #if mod 7 equal to zero then go to next line
        if (i+day)%7==0:
            print(" ")
        i+=1

#get number of days in month and starting week day
noOfDays=int(input("Enter number of days in month bw 28-31"))
weekDay=input("Input the starting day of month mon,tue,wed,thu,fri,sat,sun : ")
#pass the noOfDays,weekDay to calendar method
calendar(noOfDays,weekDay)