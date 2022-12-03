#Practise Set 3

#Q.1 Write a python programm to display a user entered name followed by Good Afternnon using input() function

str1=input("Enter Name:\n")
print("\n\nGood Afternoon",str1)


# Q.2 Print the template
Name=input("Enter Youtr Name:")
Date=input("Enter Date:\n")
letter='''\n\nDear <!Name>
\tYou are selected!
<!Date>'''

letter=letter.replace("<!Name>",Name)
letter=letter.replace("<!Date>",Date)
print(letter)

# Q.3 Write a python program to detect double space in the string
str3="Hey Suraj  Good Morning"
rs=str3.find("  ")
print(rs)

# Q.4 Replace the Double spaces in problem3 with single spaces
print(str3.replace("  "," "))

# Q.5 Use Escape character sequence
str4="Dear\tSuraj,make python.strong!"
print(str4)
