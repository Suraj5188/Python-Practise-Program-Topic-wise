#Local Global in python

#global Variable
a=10

def func1():

    #if we want here a global variable then we use global keyword
    global a
    print(a)

    #local Variable
    a=4
    print(a)

func1()
print(a)
