#generate prdered list , node class and initialize elements and next address of list

class Node:
    #initialize elements
    def __init__(self,initdata=None):
        self.head= initdata
        self.next = None


#created an unordered list class where we implement insert ,delete ,search operation
class OrderedList:

    #initialize head as none when 1st call is there
    def __init__(self):
        self.head = None
    #check if list is empty or not
    def isEmpty(self):
        return self.head == None

    #insert element at end of list
    def add(self,item):
        global size
        temp = Node(item)
        if self.head is None:
            self.head=temp
            size+=1
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=temp
            size+=1

    #display all element in list
    def displayAll(self):
        current=self.head
        while current:
            print(current.head,end=" ")
            current=current.next


    #display file element
    def fDisplay(self):
        current=self.head
        temp=""
        while current:
            temp=temp+current.head+" "
            current=current.next
        return temp

    #search element in list
    def search(self,item):
        current=self.head
        found=False
        while current and found is False:
            if current.head==item:
                found=True
            else:
                current=current.next

        return found

    #remove element from list
    def remove(self,item):
        current=self.head
        if current.head==item:
            self.head=current.next
            current=None
            return

        while current is not None:
            if current.head==item:
                break
            else:
                previous=current
                current=current.next

        if current==None:
            raise ValueError("Data is not in list")
        previous.next=current.next
        current=None

    @staticmethod
    def bubbleSort(bList):
        for i in range(len(bList)):
            for j in range(i+1,len(bList)):
                if bList[i]>bList[j]:
                    temp=bList[i]
                    bList[i]=bList[j]
                    bList[j]=temp

        return bList




#create object of class unOrdered List
myList=OrderedList()
size=0
file=input("Enter file name ")
#opening a file in read manner
with open(file) as f:
    #read lines in the file
    lines=f.readlines()
    for line in lines:
        #split a line into words
        words=line.split()
        for word in words:
            #insert word into list using method call
            myList.add(word)
    #size of list is
    print("Size of list : ",size)
    #display method call
    myList.displayAll()

    #get word from user to search in  list
    word=input("\nEnter a word to search in list : ")
    if myList.search(word):
        myList.remove(word)
        print("Element ",word ," is deleted from list !")
    else:
        print("Element ",word," is not found !")
    myList.displayAll()

    fname="output.txt"
    fwrite=open(fname,"w+")
    a=myList.fDisplay()
    a=list(a.split(" "))
    a=myList.bubbleSort(a)
    a=str(a)
    print("\n In ascending order : ",a)
    fwrite.write(a)
    fwrite.close()
    print("Created output.txt file ")