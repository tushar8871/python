# Generate utility class which contain all static methods
import datetime
import math

class Utility:

    #generate anagram method to valid strings if it is anagram or not
    @staticmethod
    def validAnagram(str1,str2):
        if sorted(str1)==sorted(str2): #used sorted method to sort string
            return True
        else:
            return False


    #find prime number between range 0-1000
    @staticmethod
    def primeNumber(initial,end):
        resultList=[]
        try:
            for i in range(initial,end,1):
                count=0
                for j in range(initial,i,1):
                    if i%j==0:
                        count+=1

                if count==1:
                    resultList.append(i)
        except Exception:
            print("Modulo divide by error")
        return resultList


    #Validate if number is palindrome or not
    @staticmethod
    def palindrome(number):
        temp=number
        sum=0
        while temp!=0:
            remainder=temp%10
            sum=sum*10+remainder
            temp=int(temp/10)

        if sum==number:
            print(number," is palindrome !")
        else:
            print("Not palindrome !")


    #Create list
    @staticmethod
    def createList(bList):
        number=int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            bList.append(int(input()))
        return bList


    #binary search method to search element in list , low=lowest value and high = highest value
    @staticmethod
    def binarySearch(bList,low,high,num):
        if high>=low:
            mid=int((low+high)/2)
            if bList[mid]==num:
                return mid
            elif bList[mid]>num:
                return Utility.binarySearch(bList,low,mid-1,num)
            else:
                return Utility.binarySearch(bList,mid+1,high,num)
        else:
            return -1


    #function for insertion sort
    @staticmethod
    def insertionSort(bList):
        for i in range(len(bList)):
            temp=bList[i]
            j=i-1
            while j>=0 and temp<bList[j]:
               bList[j+1]=bList[j]
               j-=1
            bList[j+1]=temp

        return bList


    #function for bubble sort
    @staticmethod
    def bubbleSort(bList):
        for i in range(len(bList)):
            for j in range(i+1,len(bList)):
                if bList[i]>bList[j]:
                    temp=bList[i]
                    bList[i]=bList[j]
                    bList[j]=temp

        return bList

    #function to search element which user thinks
    @staticmethod
    def findNumber(low,high):
        mid=int((low+high)/2)
        print("Press 1 for greater than , 2 for less than and 0 for match : ",mid)
        choice=int(input())
        if choice==1:
            Utility.findNumber(mid+1,high)
        elif choice==2:
            Utility.findNumber(low,mid-1)
        elif choice==0:
            low=mid
            high=mid
            print("Number is : ",low)


    #function to read file and search a word in that file
    @staticmethod
    def readFile(file,word):
        #try except block needed if file not found exception occurs
        try:
            #open file in read
            with open(file) as rf:
                #read lines in file
                readFile=rf.readlines()
                for index in readFile:
                    #checking if word is present or not in file
                    if word in index:
                        #if it present then return true
                        return True
                return 0
        except Exception:
            print("File not found ")

    #function to sort string using merge sort
    @staticmethod
    def mergeSort(bList):
        k=0
        if len(bList)>1:
            #calculate mid
            mid=int(len(bList)/2)
            #create two temporary list
            left=bList[:mid]
            right=bList[mid:]

            #recursively break list until it didnt  have 2 elements
            Utility.mergeSort(left)
            Utility.mergeSort(right)
            #initailize i and j for compariong list element
            i=j=0

            while (i<len(left)) and (j<len(right)):
                if left[i]<right[j]:
                    bList[k]=left[i]
                    i+=1
                    k+=1
                else:
                    bList[k]=right[j]
                    j+=1
                    k+=1

            #if any of element left in temp list then add here
            while i<len(left):
                bList[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                bList[k]=right[j]
                j+=1
                k+=1

        return bList

    #function for vending machine
    @staticmethod
    def vendingMachine(amount):
        #list of notes
        notes=[1000,500,200,100,50,20,10,5,2,1]
        #counter for each notes
        countNotes=[0,0,0,0,0,0,0,0,0,0]
        count=0
        #Zip is used for mapping of two array
        for i,j in zip(notes,countNotes):
            if amount>=i:
                j=int(amount/i)
                amount=amount-j*i
                print(i," : ",j)


    #function to find day of that date
    @staticmethod
    def dayWeek(date):
        day,month,year=(int(i) for i in date.split("/"))
        print(day , month , year)
        y0 = (year-(14-month ) / 12)
        x  = (y0 + (y0/4) -(y0 /100) + (y0 /400))
        m0 = (month + 12 * ((14 - month ) / 12))
        d0 = int((day + x + (31*m0 / 12))%7-1)
        print(d0)
        if d0==0:
            print("Sunday")
        elif d0==1:
            print("Monday")
        elif d0==2:
            print("Tuesday")
        elif d0==3:
            print("Wednesday")
        elif d0==4:
            print("Thursday")
        elif d0==5:
            print("Friday")
        elif d0==6:
            print("Saturday")

    #function to convert temprature from celsius to farheniet and vice versa
    @staticmethod
    def tempConversion():
        print("Enter your choice : \n 1. farheniet to celsius \n 2. celsius to farheniet")
        choice=int(input())

        if choice==1:
            temprature=int(input("enter temprature between 32-212"))
            if temprature>=32 and temprature<=212:
                return ((temprature-32)*5/9)
            else:
                print("Enter value bw 32-212 F")
        else:
            temprature=int(input("enter temprature between 0-100"))
            if temprature>=0 and temprature<=100:
                return ((temprature*9/5)+32)
            else:
                print("Enter value bw 0-100 C")


    #generate function to calculate monthly payement of an employee
    @staticmethod
    def monthPayment(year,amount,rate):
        r=(rate/(12*100))
        totalMonth=12*year

        monthPay=((amount*r)/(1-((1+r)**(-totalMonth))))
        return monthPay

    #generate square root of number using newton's method
    @staticmethod
    def squareRoot(number):
        epsilon=float(1e-15)
        t=number
        while abs(t-number/t)>epsilon*t:
            t=float((number/t +t)/2)

        print("Square root of number",number," is :",t )

    #reverse of string
    @staticmethod
    def reverse(bString):
        str=""
        for i in bString:
            str=i+str

        return str

    #generate binary number from given number
    @staticmethod
    def decimalBinary(number):
        binaryString=""
        temp=number
        while temp!=0:
            remainder=temp%2
            binaryString+=str(remainder)
            temp=int(temp/2)
        binaryString=Utility.reverse(binaryString)
        return binaryString


    #function to swap nibbles and generate decimal number
    @staticmethod
    def swapNibbles(bNumber):
        return ((bNumber & 0x0F) << 4 | (bNumber &0xF0) >> 4)


    #function to check if number is power of 2 or not
    @staticmethod
    def powerOf2(number):
        sum=0
        i=1
        while i < number:
            if sum > number:
                return 0
                break
            elif sum == number:
                return 1
                break
            else:
                sum=2**i
                i+=1


#main function
def main():

    choice=int(input("Enter your choice \n 1. Anagram Detection \n 2. Prime Number in range \n"
                    " 3. Binary Search of Integer \n 4. Binary search for string \n 5. Insertion"
                    "sort for integer \n 6. Insertion sort for string \n 7. Bubble sort for integer \n"
                    " 8. Bubble sort for string \n 9. Find element b/w range \n 10. search word in file \n"
                    " 11. Merge sort \n 12. Vending machine \n 13. Day of week \n 14. Temprature Conversion"
                    "\n 15. Monthly payment \n 16. sqrt nonNegative number \n 17. Decimal to binary \n "
                    "\n 18. Swap nibbles \n"))

    if choice==1:
        #angaram validation  get input from user
        str1=input("Enter string 1 : ")
        str2=input("Enter string 2 : ")
        #check if it is valid or not
        if (Utility.validAnagram(str1,str2)):
            print("String is anagram ",str1,str2)
        else:
            print("String is not anagram")

    elif choice==2:
        #find prime number between 0-1000
        num1=int(input("Enter initial number 1 to find prime number"))
        num2=int(input("Enter last number "))
        #get elements in list
        resultList=Utility.primeNumber(num1,num2)
        print(resultList)
        #validate if number is palindrome or not
        num=int(input("Enter number to check if it is palindrome or not "))
        Utility.palindrome(num)

    elif choice==3:
        #genrate list to search
        bList=[]
        bList=Utility.createList(bList)
        #Binary search for an integer
        length=len(bList)
        num=int(input("Enter number to search in list : "))
        res=Utility.binarySearch(bList,0,length-1,num)
        if res!=-1:
            print("Element found at position ",res)
        else:
            print("Not found ")

    elif choice==4:
        #genrate list to search element
        bList=[]
        print("Enter elements in ascending order and between A-Z")
        number=int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            bList.append(input())
        #Binary search for string
        length=len(bList)
        char=input("Enter string to search in list : ")
        res=Utility.binarySearch(bList,0,length-1,char)
        if res!=-1:
            print("Element found at position ",res)
        else:
            print("Not found ")

    elif choice==5:
        #Sort list element using insertion sort
        #generate list
        bList=[]
        bList=Utility.createList(bList)
        #sort list
        bList=Utility.insertionSort(bList)
        print("Sorted list : ", bList)

    elif choice==6:
        #genrate list to sort element
        bList=[]
        print("Enter elements between A-Z")
        number=int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            bList.append(input())
        #sort list using insertionSort
        bList=Utility.insertionSort(bList)
        print("Sorted list : ", bList)

    elif choice==7:
        #Sort list element using bubble sort
        #generate list
        bList=[]
        bList=Utility.createList(bList)
        #sort list
        bList=Utility.bubbleSort(bList)
        print("Sorted list : ",bList)

    elif choice==8:
        #genrate list to search element
        bList=[]
        print("Enter elements in ascending order and between A-Z")
        number=int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            bList.append(input())
        #sort list using insertionSort
        bList=Utility.bubbleSort(bList)
        print("Sorted list : ", bList)

    elif choice==9:
        #get inputfom user upto which you want to guess a number
        number=int(input("Enter number upto which you want to guess any one number : "))
        Utility.findNumber(0,number)

    elif choice==10:
        #read word from file and search a word in that file
        file=input("Enter file : ")
        word=input("Enter word to be search in file : ")
        res=Utility.readFile(file,word)
        if res:
            print("Found word ")
        else:
            print("Not found ")

    elif choice==11:
        #genrate list to search element
        bList=[]
        print("Enter elements")
        number=int(input("Enter how many elements you want to add : "))
        print("Enter elements : ")
        for i in range(number):
            bList.append(input())
        #sort list using Merge Sort
        bList=Utility.mergeSort(bList)
        print("Sorted array : ",bList)


    elif choice==12:
        #get amount from user
        amount=int(input("Enter amount in Rs : "))
        result=[]
        result.append(Utility.vendingMachine(amount))

    elif choice==13:
        #get date from user
        date=input("Enter date as dd/mm/yyyy: ")
        Utility.dayWeek(date)

    elif choice==14:
        #get temprature from user
        res=Utility.tempConversion()
        print("Temprature is : ",res)

    elif choice==15:
        #get years ,principal amount,rate of intrest from user
        year=int(input("Enter year : "))
        amount=int(input("Enter principal amount : "))
        rate=int(input("Enter intrest rate : "))
        monthPay=Utility.monthPayment(year,amount,rate)
        print("Monthly payement is : ",monthPay)

    elif choice==16:
        #Get number from user to calculate sqrt of number using newton's method
        number=int(input("Enter number : "))
        Utility.squareRoot(number)

    elif choice==17:
        #get number from user
        number=int(input("Enter decimal number : "))
        binary=Utility.decimalBinary(number)
        print("Binary number is : ",binary)

    elif choice==18:
        #get input from user and convert into binary then swap nibbles
        number=int(input("Enter decimal number : "))
        binary=Utility.swapNibbles(number)
        print("After swap decimal number is : ",binary)
        #now generate resultant number is power of 2
        result=Utility.powerOf2(binary)
        if result==1:
            print("Resultant Number is power of 2 ",binary)
        else:
            print("Resultant number is not power of 2 ",binary)




main()