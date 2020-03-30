#Generate permutation of string

#function to swap element of string
def swap(tempList,start,count):
    #swapping element in list
    temp=tempList[start]
    tempList[start]=tempList[count]
    tempList[count]=temp
    #return list of string
    return tempList

#generate permutation of string
def strPermutation(Str,start,end):
    count=0
    #if start and equal to length of string then print string
    if (start==end-1):
        print(Str)
    else:
        for count in range(start,end):
            #Put String in list to generate permutation
            tempList=list(Str)
            #call swap function to swap element of string
            swap(tempList,start,count)
            #recursive call until found all string
            strPermutation("".join(tempList),start+1,end)
            swap(tempList,start,count)

#Get input from user
Str=input("Enter string : ")
#find length of string
strLength=len(Str)
#call function to generate permutation of string
strPermutation(Str,0,strLength)