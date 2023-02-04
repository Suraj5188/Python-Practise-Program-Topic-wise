#OOPS
'''
class student:
    pass

#object1
suraj=student()
suraj.name="suraj"
suraj.std="TY"
suraj.section=1


#object2
prasad=student()    


print(f"{suraj.name}\n{suraj.section}")
'''

class Employee:

    #This No of leaves are sharable every object if we defined in class
    no_of_leaves=6
    
    pass

suraj=Employee() 
prasad=Employee()

suraj.name="suraj"
suraj.salary=100000
suraj.designation="Data Scientist"

#if we have to change the no of leave then we have to use class name 
Employee.no_of_leaves=10

#if we try to change the particular value of object then it will create new instance variable of that object
suraj.no_of_leaves=15

#print(suraj. __dict__)

print(Employee. __dict__)

prasad.name="Prasad"
prasad.salary=100000
prasad.designation="Data Analysis"


print(f"{suraj.name}\n{suraj.salary}\n{suraj.no_of_leaves}")