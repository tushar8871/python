#get power from user to calculate exponent of 2

power=int(input("Enter power to calculate exponent"))
#genrate exponent of 2
result=2**power
table=0
index=1

#print table of 2 upto that exponentresult
for index in range(1,result,1):
    if table==result:
        break
    else:
        table=2*index
        print(table)