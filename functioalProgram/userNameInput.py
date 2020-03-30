#Take input from user and validate length of name is greater than 3 or not

userName=input("Enter your name : ")
lengthOfName=len(userName)

if lengthOfName>=3 :
    print (f"Hello {userName} , How are you ? ")
else:
    print ("userName at least contain 3 characters")