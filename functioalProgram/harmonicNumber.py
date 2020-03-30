#Generate n harmonic value

number=int(input("Enter number"))
sum=0

for index in range(1,number,1):
    sum+=1/index
    print(f'1/{index}')

print(sum)