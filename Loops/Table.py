#Task:- to print the multiplication table of a number n.

print("multiplication Table")

number = int(input("Enter A number: ")) #input the number 

#11 is becuse as 10 will not involve in the loop 
for n in range(1, 11):
    print(n, "X", number,"=", n*number) #output is 1 X 2 = 2 like this 

