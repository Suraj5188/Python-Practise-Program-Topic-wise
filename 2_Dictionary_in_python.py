#Practise set 5

# Q.1 Write a program indictionary with hindi name & translation in english
'''
mydict={"Hindi":"Hindi1",
    "kitab":"Book",
    "pankha":"Fan",
    "Dabba":"Box",
    "Phulo":"Flowers",
    "sona":"Gold"}

#print("Options are",mydict.keys())
dict_input=input("Enter the hindi words:\n")

#This line will throw error if dictionary is not present 
#print("Your hindi words to english:\n",mydict[dict_input])

#This line will throw error if dictionary is not present
print(f"Your hindi word to english:{mydict.get[dict_input]}")

'''
# Q.2 Write a program to input eight numbers from the user & dispaly all the unique numbers(once)
'''
n1=int(input("Enter Numbers\n"))
n2=int(input("\n"))
n3=int(input("\n"))
n4=int(input("\n"))
n5=int(input("\n"))
n6=int(input("\n"))
n7=int(input("\n"))
n8=int(input("\n"))

s={n1,n2,n3,n4,n5,n6,n7,n8}
print(s)
'''

# Q.3 Can we print have a set with 18(int) & 18(string) as a value in it
'''
set1={18,"18"}
print(set1)
'''
#Q.4 What will be the length following set s
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

# Q.5 What is the type 
s={} 
print(type(s))

# Q.6 Create an empty dictionary. Allow 4 friends to enter their favuorite language as values & use the keys as names& names as a unique

friend={}
frd_input1=input("Enter Their Favourite Language Suraj:\n")
frd_input2=input("Enter Their Favourite Language Prasada:\n")
frd_input3=input("Enter Their Favourite Language Sambhaji:\n")
frd_input4=input("Enter Their Favourite Language Om:\n")
friend['Suraj']=frd_input1
friend['Prasad']=frd_input2
friend['Sambhaji']=frd_input3
friend['Om']=frd_input4


print(type(friend))
print(friend)

# Q.7 If names of friends are same what will be happen in problem 6 

# Q.8 If language of two friends language are same then what will happen in prolem 6
