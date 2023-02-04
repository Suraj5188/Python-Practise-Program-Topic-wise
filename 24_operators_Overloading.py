#Opreators Overloading in python

from __future__ import division
from ast import Div
from operator import truediv


class number:
    def __init__(self, num):
        self.num=num

    def __add__(self, num2):
        print("Let's Add")
        return self.num+ num2.num
    
    def __mul__(self, num2):
        print("Let's Mul")
        return self.num* num2.num

    def __truediv__(self,num2):
        print("Let's Div")
        return self.num/num2.num



n1=number(24)
n2=number(2)

sum=n1+n2
mul=n1*n2
div=n1/n2

print(sum)
print(mul)
print(div)