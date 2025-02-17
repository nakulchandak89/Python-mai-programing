#this script will enshure the provided number is palandrom or not (eg: 56, 65) this pair are palandrom


num1 = int(input("Enter Number 1: "))
num2 = int (input("Enter the Number 2: "))

num_str = str(num1)
num_str2 = str(num2)

rev = num_str[::-1]

if rev == num_str2:
    print("is palandrom")

else:
    print("Is not an palandrom")


#can we do the same for the string as well 

str1 = str(input("Enter and string: "))
str2 = str(input("Enter an another string: "))

str_rev = str1[::-1]

if str_rev == str2:
    print("is an palandrom ")

else:
    print("is not an palandrom")

    
