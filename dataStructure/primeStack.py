#generate prime number and insert element in stack using list
#creating class stack
class Stack:
    #initialized list elements
    def __init__(self):
        self.elements=[]

    #check if stack is empty or not
    def isEmpty(self):
        return self.elements==[]

    #add element in stack
    def push(self,item):
        self.elements.append(item)

    #delete an element from stack
    def pop(self):
        self.elements.pop()



#generate prime number in range 0-1000 and store it into 2D Array
#method to create prime number
def primeNumber(initial,end):
    #create a list to store prime number in 0-100,100-200 and so-on
    resultList=[]
    try:
        #initialize countt because when we generate prime number between 0-100 then we have to initialize
        #initial from 100 not to 1
        countt=1
        #loop executed until initial is less than  end
        while initial<end:
            #initialize temp to stop execution of loop upto 100,200 ,etc to create seperate list
            temp=100*countt
            #creating object of class Stack
            stObj=Stack()
            #execute loop utp temp and generate number
            for k in range(1,temp):
                count=0
                for j in range(1,k+1):
                    #check K mod j =0 then increment count
                    #count is incremneted because prime number only divided by itself or one
                    if k%j==0:
                        count+=1
                if count==2:
                    #when we add number from 2nd execution already stored number will not be stored
                    if (k > initial):
                        #push element in list using stack
                        stObj.push(k)
            #append list of prime no into main list
            resultList.append(stObj.elements)
            countt+=1
            initial=temp
    except Exception:
        print("Modulo divide by error")
    return resultList

#mehod to check element is anagram or not
def validAnagram(listt):
    #create anagram list
    aList=[]
    #execute loop to check if element is present in list
    for i in listt:
        for j in listt:
            #check if element in list is angaram is or not
            if sorted(str(i))==sorted(str(j)):
                aList.append(i)
    return aList



#get range from user to find prime number
initial=int(input("Enter initial vlaue of range : "))
end=int(input("Enter end vlaue of range : "))
#method call and store into listt
listt=primeNumber(initial,end)
listt=validAnagram(listt)
#print list of prime number
print("Prime Number in 2D array are : \n " ,listt)