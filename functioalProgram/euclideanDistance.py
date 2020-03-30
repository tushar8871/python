#Generate euclidean distance
import math

#read x and y from user
x=int(input("Enter x :"))
y=int(input("Enter y :"))

#calculate euclidean distance using math function
distance=math.sqrt(math.pow(x,2)+math.pow(y,2));
#display distance
print(distance)