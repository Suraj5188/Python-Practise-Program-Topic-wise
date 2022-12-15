#Fuction in python

def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p    

marks1=[60,70,80,90]
'''
per=(sum(marks)/400)*100
we can also use to''' 
per1=percent(marks1)

marks2=[55,65,85,90]
per2=percent(marks2)

print(per1,per2)

'''
#For Understanding
def suraj():
    return "hello"

str=suraj()  + "Data Scientist"
print(str)
'''

#Write a program to greet a user with "Good Day" using function

def greet(name):
    return print(name + " Good Day")

greet("suraj")
greet("Santosh")

def greet2(name1,name2):
    return print(name1+name2)

greet2("Python","Data Scientist")
greet2(10,20)


def greet3(name="Hello"):
    return print(name + " Suraj")

greet3("Good Morning")

