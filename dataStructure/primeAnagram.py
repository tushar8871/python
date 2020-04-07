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
            list1=[]
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
                        list1.append(k)
            #call method valid anagram to check if num is anagaram or not
            #if yes then add to list
            list1=validAnagram(list1)
            #append list of prime no into main list
            resultList.append(list1)
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
    for i in list1:
        for j in list1:
            #check if element in list is angaram is or not
            if i==reverseNum(j):
                aList.append(i)
    return aList



#get range from user to find prime number
initial=int(input("Enter initial vlaue of range : "))
end=int(input("Enter end vlaue of range : "))
#method call and store into listt
listt=primeNumber(initial,end)
#print list of prime number
print("Prime Number in 2D array are : \n " ,listt)