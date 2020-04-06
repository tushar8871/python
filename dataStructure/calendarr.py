#genrate calendar without usong module

#method to generate calendar
def calendar(noOfDays,weekDay):
    #create list of week day
    week=["sun","mon","tue","wed","thu","fri","sat"]
    #create list for dates
    date=[' ']*(noOfDays+1)
    for dayDate in range(1,(noOfDays+1)):
        date[dayDate]=dayDate
    #check if weekDay is same or not
    for day in range(len(week)):
        if weekDay==week[day]:
            break

    #print days
    print("Su Mo Tu We Th Fr Sa")
    #print dates
    for i in range(day):
        print("  ",end=" ")
    i=1
    while (i<=noOfDays):
        #print the dates
        if date[i]<10:
            print("",date[i],end=" ")
        else:
            print(date[i],end=" ")
        #if mod 7 equal to zero then go to next line
        if (i+day)%7==0:
            print(" ")
        i+=1

#get number of days in month and starting week day
noOfDays=int(input("Enter number of days in month bw 28-31"))
weekDay=input("Input the starting day of month mon,tue,wed,thu,fri,sat,sun : ")
if noOfDays >= 28 and noOfDays <= 31:
    #pass the noOfDays,weekDay to calendar method
    calendar(noOfDays,weekDay)
else:
    print("Enter correct value between 28 to 31 ! ")