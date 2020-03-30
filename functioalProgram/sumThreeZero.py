#Sum of three integer to be zero

#get element size from user
listSize=int(input("enter size of list : "))
integerArray=[]

#enter elements in list
print("Enter elements in list ")
for index in range(listSize):
    integerArray.append(int(input()))

#initialize empty list
sumZero=[]
for index in range(0,listSize):
    for index1 in range(index+1,listSize):
        for index2 in range(index1+1,listSize):
            #check if sum is zero then store triplet in sumZero list
            if (integerArray[index]+integerArray[index1]+integerArray[index2]) == 0:
                sumZero.append(integerArray[index])
                sumZero.append(integerArray[index1])
                sumZero.append(integerArray[index2])

print("Triplets are : ",sumZero)