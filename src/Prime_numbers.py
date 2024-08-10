
number = int(input("Enter a number: "))
flag = False
for i in range(2,number): #
    if number % i == 0:
        flag = True

if flag==True:
    print("Not prime")
else:
    print("prime")






