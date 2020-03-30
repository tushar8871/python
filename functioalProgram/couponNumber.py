#Genrate distinct coupon number using random
import random

#empty list is initialized
randomCouponNumber=[]

#function to generate coupon number
def genreateCouponNumber(totalNumber):
    for index in range(0,totalNumber+1,1):
        #generate coupon number
        couponNumber=random.randint(0,totalNumber)
        for count in range(0,index,1):
            #check if coupon is already exist in list or not
            if couponNumber in randomCouponNumber:
                break;
            else:
                #if not then add coupon number in list
                randomCouponNumber.append(couponNumber)


#get input from user to genearte n random coupon number
totalNumber=int(input("Enter number upto you want to generate distinct number randomly : "))
genreateCouponNumber(totalNumber)
#print random coupon number in list
print(randomCouponNumber)