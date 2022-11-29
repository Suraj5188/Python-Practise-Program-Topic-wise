#Shallow copy

#............shallow copy.............

list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1
print(list1,list2)
print(list1[1])
print(list2[1])
print("\n")
#if we try to change the value of list2 then it will change also list1
list2[1]=100
print(list2)
print(list1)
print("\n")

#To avoid that we use copy
#creating new list for understanding purpose

list3=[100,200,300,400,500]
list4=list3.copy()
print(list3)
print(list4)
print("\n")

#now if we try to change the value now it will not change both the list
list4[1]=3500
print(list4)
print(list3)
print("\n")

#now we are creating the nested list
list5=[[10,20,30,40,50,60,70,80,90,100],[5,10,15,20,25,30,35,40,45,50]]
list6=list5.copy()
print(list5)
print(list6)

print(list5[1][0])
list5[1][1]=1000
print(list5)
print(list6)

print("\n")

list7=[[1,2,3,4,5],[100,200,300,400,500]]
list8=list7.copy()
list7.append([10,20,30,40])

print(list7)
print(list8)