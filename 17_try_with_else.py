#Try with else
try:
    i=int(input("Enter number:"))
    c=1/i
except Exception as e:
    print(e)
else:
    print("succussefull !")