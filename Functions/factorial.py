# WAF to find the factorial of n. (n is the parameter)

def fact(x):
   #this is the basic condition for the factorial
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1) #Recursion (a function is call in itselft)
    


x = int(input("Enter Number: ")) #input is stored and passed 
print("factorial of",f"{x} is",fact(x)) #function call

