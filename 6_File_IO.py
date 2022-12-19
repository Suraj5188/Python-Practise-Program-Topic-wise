#File IO

#Read The Content file
f=open("suraj.txt","r")

data456=f.read()
#data456 is the variable name we can choose any varible name
print(data456)


data456=f.readline()
print(data456)

f.close()


#Write the content into the file

f=open("suraj_2.txt","a")
f.write("Please Keep going your learning in data scientist")
f.close()


#With statement

with open("suraj.txt","r") as f:
    a=f.read()

with open("suraj.txt","w") as f:
    a=f.write("python")
    print(a)
