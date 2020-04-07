#generate prime number in range 0-1000 and store it into 2D Array

#generate queue class
class Queue():

    # __init__ function
    def __init__(self):
        self.front = 0
        self.size = 0
        self.rear = 0
        self.queue = []

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
        self.rear+=1


    #display all element in queue
    def display(self):
        print("Elements in queue is : ")
        while self.front!=self.rear:
            print(self.queue[self.front])
            self.front+=1




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
            qu=Queue()
            #list1=[]
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
                        qu.enqueue(k)
            #append list of prime no into main list
            qu.queue=validAnagram(qu.queue)
            resultList.append(qu.queue)
            countt+=1
            initial=temp
    except Exception:
        print("Modulo divide by error")
    return resultList

#method to reverse a number
def reverseNum(number):
    revNum=0
    rem=0
    #check if number is greater then 0
    while number>0:
        #modulo number by 10 to get rem
        rem=number%10
        #store rem into revNum
        revNum=revNum*10+rem
        number=number//10
    #return revNum
    return revNum

#mehod to check element is anagram or not
def validAnagram(list1):
    #create anagram list
    aList=[]
    #execute loop to check if element is present in list
    for i in range(len(list1)):
        for j in range(len(list1)):
            iVariable=list1[i]
            jVariable=reverseNum(list1[j])
            #check if element in list is angaram is or not
            if iVariable==jVariable:
                aList.append(jVariable)
                break
    return aList



#get range from user to find prime number
initial=int(input("Enter initial vlaue of range : "))
end=int(input("Enter end vlaue of range : "))
#method call and store into listt
listt=primeNumber(initial,end)
#print list of prime number
print("Prime Number in 2D array are : \n " ,listt)