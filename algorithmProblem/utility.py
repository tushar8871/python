# Generate utility class which contain all static methods

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



#main function
def main():

    choice=int(input("Enter your choice \n 1. Anagram Detection \n 2. Prime Number in range \n"
                    " 3. Binary Search of Integer \n 4. Binary search for string \n 5. Insertion"
                    "sort for integer \n 6. Insertion sort for string \n 7. Bubble sort for integer \n"
                    " 8. Bubble sort for string \n "))

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
        #genrate list to search element
        bList=[]
        print("Enter elements in ascending order and between A-Z")
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


main()