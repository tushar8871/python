#generate prime factors of number

number=int(input("enter number : "))

for index in range(2,number,1):
    count=0
    for index2 in range(1,number,1):
        if (index%index2) == 0 and (number%index) == 0 :
            count+=1

    if count == 2:
        print(index)