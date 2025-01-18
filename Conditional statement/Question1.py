# performing the n numbere of opration 

number = int(input("Enter any number between 1 to 100: "))

if number % 3 == 0:
    print("Weird")
elif number % 2 == 0 and 1 <= number <= 5:
    print("Not Weird")
elif number % 2 == 0 and 6 <= number <= 20:
    print("Weird")
elif number > 20 and number % 2 == 0:
    print("Not Weird")



