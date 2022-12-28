#Exception Handling in python

from logging import exception


try:
    num=int(input("Enter Number:\n"))
    div=1/num
    if(num>=10):
        print(f" You Entered the number is {num}")
        print(div)
    else:
        print(f"You Enterd smaller number is {num}")
except Exception as e:
    print(f"Incorrect Input! {e}")
