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
                print(bList)
                i+=1
                k+=1
            while j<len(right):
                bList[k]=right[j]
                print(bList)
                j+=1
                k+=1

        return bList



#main function
def main():

    choice=int(input("Enter your choice \n 1. Anagram Detection \n 2. Prime Number in range \n"
                    " 3. Binary Search of Integer \n 4. Binary search for string \n 5. Insertion"
                    "sort for integer \n 6. Insertion sort for string \n 7. Bubble sort for integer \n"
                    "8. Bubble sort for string \n 9. Find element b/w range \n 10. search word in file \n"
                    "11. Merge sort"))

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



main()