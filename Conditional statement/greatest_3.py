#this code is for cheackiing the Greatest of 3 number 

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if(num1 > num2 and num1 > num3):
    print(num1,"is greater than",nnum2,"and",num3)
elif(num1 < num2 and num2 > num3):
    print(num2,"is greather than",num1,"and",num3)
elif(num1 < num3 and num2 < num3):
    print(num3,"is greather than",num1,"and",num2)
else:
    print("Enter number only")

    