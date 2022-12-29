#Loops in python
'''
i=0
while i<=10:
    print("Good morning Suraj")
    i =i+1
'''

# Q Write a program to print 1 to 50 using while loop
'''
num=int(input("Enter Number you want :"))
print("\n")
while(num<=50):
    print(num)
    num=num+1
'''

# Q
'''
i=0
while i<5:
    print("Suraj", + i)
    i=i+1
'''
#Q Write a program to print the content using while loop
'''
str1=input("Enter the string1:\n")
str2=input("Enter the string2:\n")
str3=input("Enter the string3:\n")
str4=input("Enter the string4:\n")

list=[str1,str2,str3,str4]
i=0
while i<len(list):
    print(list[i])
    i=i+1
    
'''

#For Loop
'''
list=["Apple","Banana","Watermellon","Grahes"]
i=0
for item in list:
    print(item)

'''

#Range function

#start,stop,skip
'''
for i in range(1,8,2):
    print(i)
'''
#For Loop with else
'''
list2=[10,20,30,40,50,60]
for item in list2:
    print(item)
else:
    print("Done")'''

#Break Statement
'''
for i in range(10):
    print(i)
    if i==5:
        break
    else:
            print("Hello")
'''
# Continue statement
'''
for i in range(10):
    if i==5:
        continue
    print(i)

'''

#Pass Statement

i=4
def sum(a,b):
    pass
if i>0:
    pass
    print("Suraj Keep Going!")