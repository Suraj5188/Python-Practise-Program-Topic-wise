#Practise Set 4

# Q.1 Write a python program to store seven fruits entered by the user in  the list

list1=input("Enter 1st Fruits:\n")
list2=input("Enter 2nd Fruits:\n")
list3=input("Enter 3rd Fruits:\n")
list4=input("Enter 4th Fruits:\n")
list5=input("Enter 5th Fruits:\n")
list6=input("Enter 6th Fruits:\n")
list7=input("Enter 7th Fruits:\n")
rs=[list1,list2,list3,list4,list5,list6,list7]
print(rs)

# Q.2 Write a program to accept marks of 6 students & display them in sorted orderd

s1=int(input("1st Students marks:\n"))
s2=int(input("2nd Students marks:\n"))
s3=int(input("3rd Students marks:\n"))
s4=int(input("4th Students marks:\n"))
s5=int(input("5th Students marks:\n"))
s6=int(input("6th Students marks:\n"))

rs2=[s1,s2,s3,s4,s5,s6]
rs2.sort()
print(rs2)

# Q.3 Checked that tuple cannot be changed in python

c=(30,60,90,120)
c[0]=100
print(c)

# Q.4 Write a program sum the list of 4 numbers

list2=[40,50,60,70]
print(list2[0]+list2[1]+list2[2]+list2[3])

#Q.5 Write a programm to count the number of zeros in the following table

t1=[0,0,0,6,7,7,4,4,2,0,0]
print(t1.count(0))
