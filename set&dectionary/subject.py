#this code is to make an loop for user to add the subject and marks 

print("Enter your subject and then marks")

studentinfo = {
    
}

s1 = input("Enter your subject: ")
m1 = int(input("Enter marks of above subject:"))
studentinfo[s1] = m1

s2 = input("Enter your subject: ")
m2 = int(input("Enter marks of above subject:"))
studentinfo[s2] = m2

s3 = input("Enter your subject: ")
m3 = int(input("Enter marks of above subject:"))
studentinfo[s3] = m3

print(studentinfo)

print(type(studentinfo))