#this script checks wether the number is prime or not 

num = int(input("Enter your number: "))

if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("the number entered is non prime number")

else:
   print(f"{num} is an prime number")



