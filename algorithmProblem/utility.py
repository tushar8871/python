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

util=Utility()

def main():

    choice=int(input("Enter your choice \n 1. Anagram Detection \n 2. Prime Number in range \n"))

    if choice==1:
        #angaram validation  get input from user
        str1=input("Enter string 1 : ")
        str2=input("Enter string 2 : ")
        #check if it is valid or not
        if (util.validAnagram(str1,str2)):
            print("String is anagram ",str1,str2)
        else:
            print("String is not anagram")
    elif choice==2:
        #find prime number between 0-1000
        num1=int(input("Enter initial number 1 to find prime number"))
        num2=int(input("Enter last number "))
        resultList=util.primeNumber(num1,num2)
        print(resultList)

main()