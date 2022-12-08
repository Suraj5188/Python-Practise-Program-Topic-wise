#Recurssion function in python
'''
n=4
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)
'''
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print(factorial(5))
'''

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

f=factorial_recursive(4)
print(f)
