# Task 1: Print the elements of the list
print("Printing the list as provided:")

el = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for x in el:
    print(x)

# Task 2: Search for a number in the list and show its position
print("\nFrom the above elements, input any number to search:")

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sarch = int(input("Enter a number: "))

if sarch in num:
    position = num.index(sarch)  # Get the index of the searched number
    print(f"{sarch} is present in the list at position {position}.")
else:
    print(f"{sarch} is not present in the list.")


# the expression f"{sarch}" is part of Python's f-strings, which are a concise and readable way to format strings.