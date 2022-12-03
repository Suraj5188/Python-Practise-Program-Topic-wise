name="Suraj"
str1="Hey Suraj Good Morning"
print(type(name))
print(name+ str1)

#Concating two String
str2=name + str1
print(str2)

print(name[2])
print(name[:3])

#if we entered out of index...print(name[5])
print(name[-4:-1])
print(name[-4:-2])
print(name[:-3])

word="suraj"
print(word[1:5:2])

word2="surajgaikwad"
print(word2[1:11:3])

word3="hey suraj gaikwad"
print(word3[1:6:3])
print(len(word2))

#Count the length of the string
print(len(word3))


print(word.endswith("raj"))

#String ends with speacific character
print(str1.endswith("fg"))

#count the character in words or string
print(word.count("s"))
print(str1.count("n"))

#Capitialize the string i.e It capitialize the first letter
string1="data science"
print(word.capitalize())
print(string1.capitalize())

#find() it finds the given word & return the occurance the given string
string_1="Hey are you learning Python in data science or R or or java"
rs=string_1.find("or")
print(rs)

#replace(oldword,newword) it replaces the old word with new word
print(string1.replace("science","scientist"))
print(string_1.replace("or","&"))
