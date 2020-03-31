#Generate roots of quadratic equations
import math

#try except block is added due to divide by zero exception
try:
    #get input from user
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=int(input("Enter c : "))

    #calculate delta to find roots of expression
    delta=(b*b)-(4*a*c)
    if delta>0:
        #calculated root 1 value using expression i.e -b+sqrt(delta)/2a
        root1=((-b+math.sqrt(delta))/(2*a))
        #calculate root2 value
        root2=((-b-math.sqrt(delta))/(2*a))
        #print roots of expression
        print("Roots of x are : ",root1,root2)
    elif delta==0:
        #calculated roots when delta is equal to 0
        root1=root2=(-b/(2*a))
        print("Root of x is :",root1)
    else:
        #calculate roots when delta is less than 0 and generate complex expression
        realValue=(-b/(2*a))
        imaginaryValue=(math.sqrt(-delta)/(2*a))
        print("root 1 of expression is : ",realValue," + ",imaginaryValue,"i")
        print("root 2 of expression is : ",realValue," - ",imaginaryValue,"i")
except ZeroDivisionError:
    #if any exception occurs then print divide by zero
    print("Divide by zero error !")