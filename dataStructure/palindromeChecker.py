#check if string is palindrome or not

class Dequeue():

    # __init__ function
    def __init__(self, capacity):
        self.front =0
        self.size = 0
        self.f=0
        self.rear = capacity-1
        self.queue = [None]*capacity
        self.capacity = capacity


    #check if queue is empty or not
    def isEmpty(self):
        return self.size==0

    #check if queue is full or not
    def isFull(self):
        return self.capacity==self.size

    # Function to add an item to the queue.
    # It changes rear and size
    def enqueue(self, item):
        if self.isFull():
            print("Queue is full !")
            return
        else:
            self.queue[self.f] = item
            self.size += 1
            self.f+=1

    #remove element at first position
    def remFront(self):
        #check if queue is empty or not
        if self.isEmpty():
            print("Underflow Queue ! ")
            return
        else:
            #if deque has only one element
            if self.front==self.rear:
                temp=self.queue[self.front]
                self.front=-1
                self.rear=-1
            elif self.front==self.capacity-1:
                temp=self.queue[self.front]
                self.front=0
            else:
                temp=self.queue[self.front]
                self.front+=1
        self.size-=1
        return temp

    #remove element at last position
    def remRear(self):
                #check if queue is empty or not
        if self.isEmpty():
            print("Underflow Queue ! ")
            return
        else:
            #if deque has only one element
            if self.front==self.rear:
                temp=self.queue[self.rear]
                self.front=-1
                self.rear=-1
            elif self.rear==0:
                temp=self.queue[self.rear]
                self.rear=self.capacity-1
            else:
                temp=self.queue[self.rear]
                self.rear-=1
        self.size-=1
        return temp


def palindrome(string):
    deq=Dequeue(len(string))
    i=0
    for i in range(len(string)):
        deq.enqueue(string[i])

    while (len(string)-1)>=0:
        if deq.front==deq.rear:
            return True
        else:
            first=deq.remFront()
            last=deq.remRear()
            if first!=last:
                return False

    return True

string=input("Enter string to check palindrome ")
if (palindrome(string)):
    print("String is palindrome ")
else:
    print("String is not palindrome ")