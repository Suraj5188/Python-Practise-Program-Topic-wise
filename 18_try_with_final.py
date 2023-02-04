#Try with final
try:
    i=int(input("Enter number:"))
    c=1/i
except Exception as e:
    print(e)
    exit()
    
finally:
    print("succussefull !")