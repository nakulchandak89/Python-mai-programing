#this code is for checking if the string is palandrom of not 

'''
a palandrom is the string in which the reverse and forward both the arrengment are same 
the input should be of 3 number atlist coz 2 number are by default  palandrom 

mai ismai ak logic ak isa soch rha ki reverse kar ke index check kar lena 
'''


print("This is the code for checking the palandrom of the list")

number = []

num = int(input("Enter the number: "))
number.append(num)

num2 = int(input("Enter the number: "))
number.append(num2)

num3 = int(input("Enter the number: "))
number.append(num3)

num4 = int(input("Enter the number: "))
number.append(num4)

num5 = int(input("Enter the number: "))
number.append(num5)

print("Original list: ", number)

reverse_list = number[::-1]

if(reverse_list == number):
    print("given list is palandrom")
else:
    print("Given list is not an palandrom")






