# generate bank cash counter and
#check whether deposit or withdraw amount is deposited or not using queue

class Queue():

    # __init__ function
    def __init__(self, capacity):
        self.front = 0
        self.size = 0
        self.rear = 0
        self.queue = [None]*capacity
        self.capacity = capacity

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def enqueue(self, item):
        if self.isFull():
            print("Queue is full !")
            return
        else:
            self.queue[self.rear] = item
            self.size += 1
            self.rear+=1

    # Function to remove an item from queue.
    # It changes front and size
    def deque(self):
        if self.isEmpty():
            print("Empty")
            return
        else:
            self.front=int((self.front)%(self.capacity))
            self.queue[self.front]
            self.front += 1
            self.size = self.size -1


    #display all element in queue
    def display(self):
        print("Elements in queue is : ")
        while self.front!=self.rear:
            print(self.queue[self.front])
            self.front+=1


class Bank():
    #get number of people stand in queue
    capacity=int(input("Enter capacity of queue : "))
    #create object of queue class and generate queue of that capacity
    qu=Queue(capacity)
    accBalance=0
    i=0;
    #initailize loop until queue capcity is full
    while i != capacity:
        #initailize variables
        USERBALANCE=5000
        accBalance=USERBALANCE

        try:
            print("\n Enter your choice : \n 1. Deposit \n 2. Withdraw \n ")
            choice=int(input())

            if choice==1:
                depositAmount=int(input("Enter amount you want to deposit : "))
                accBalance+=depositAmount
                qu.enqueue(accBalance)
                print("Available Balance : ",accBalance)
                i+=1
            else:
                withdrawAmount=int(input("Enter amount you want to withdraw : "))
                if withdrawAmount>USERBALANCE:
                    print("Insufficient Balance !")
                else:
                    accBalance-=withdrawAmount
                    qu.enqueue(accBalance)
                    print("Available Balance : ",accBalance)
                    i+=1
        except Exception :
            print("Please Enter appropriate value ! ")

    #display all elements
    qu.display()

b=Bank()