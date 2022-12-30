#Decorator in Python

def func1(argument1):
    
    def func2():
        print("GooD MoRning! func2")
        argument1()
        print("Hello")
    return func2

def func4():
    print("Suraj is the data scientist")

func4=func1(func4)

func4()

