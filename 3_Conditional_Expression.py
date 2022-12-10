#Conditional statement
a=-1
if(a>=3):
    print("a is greater than 3")
if(a>=7):
    print("a is greater than 7")

if(a>=18):
    print("a is greater than 10")
else:
    print("a is not greater then 3 or 7 or 10")      

#Write a program to print yes when the age is entered by the user is greater than or equal to 18

age=int(input("Enter the age:\n"))
if(age>18 and  age<20):
    print("The age is greater than 18",+age)
elif(age==18 or age<=18):
    print("The age is equal to 18", +age)
else:
    print("The age is you entered is neigther greater 18 or equal")