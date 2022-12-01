
from ast import arg


def func1(*args):
    for item in args:
        print(item)

names=['suraj','santosh','pramod','kiran','tejas']
func1(names)

