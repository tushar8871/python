#Check if year is leap year or not

getYear=input("Enter year : ")
length=len(getYear)
year=int(getYear)

if length ==4 :
    if (year%4) == 0 and (year%100) != 0:
        print("It is a leap year ",year)
    elif (year%400) ==0 :
        print("It is a leap year ",year)
    else:
        print("It is not a leap year ",year)
else:
    print("Year mst be of length 4")