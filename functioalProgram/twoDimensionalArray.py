#Get input from user and generate 2D array

#get row and column size from user
row=int(input("enter rows size: "))
column=int(input("enter column size: "))

#initialize empty list
elementList=[]

#get elements from user
print("Enter elements : ")
for rowIndex in range(row):
    #generate array to store 1 row elements in 1 array
    twoDArray=[]
    for colIndex in range(column):
        twoDArray.append(int(input()))
    #store 1 array in list at 1 iteration
    elementList.append(twoDArray)

#display list
print(elementList)