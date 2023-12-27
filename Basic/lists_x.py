
#list

my_list = list();
my_other_list = [];

print(len(my_list))

my_list = [35,24,62,52,30,30,17]
print(len(my_list))
print(my_list)
print(my_list.count(30))

print("\n")

my_other_list = [35,1.77,"Brais","Moure"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list)

print(my_other_list[1],1)
print(my_other_list[2],2)
print(my_other_list[3],3)
print(my_other_list[-1],-1)
print(my_other_list[-2],-2)
print(my_other_list[-3],-3)
print(my_other_list[-4],-4)
#print(my_other_list[-5])

age,height,address,surname = my_other_list;
print(address)
print(age)


# list concantenation
print(my_list + my_other_list)

mylist3  = list("Hello World")
print(mylist3)

# Adding elements
print("\n")
print(my_other_list)
my_other_list.append("Sierpe")
print(my_other_list)
my_other_list.insert(1,"Red")
print(my_other_list)

# Delete an item from in the list
my_other_list.remove("Red")
print(my_other_list)

print("\n")

# Now I'll use "pop"

print(str(my_list))
print(my_list.pop())
print(str(my_list))

my_First_Pop_Element = my_list.pop(2)

print(my_First_Pop_Element)
print(str(my_list))

del my_list[2]

print(str(my_list))

#Copy is used to copy the list
print("\n")
my_new_list = my_list.copy();
print(my_new_list)
my_new_list.reverse()

print(my_new_list)
#Sorting
my_new_list.sort();
print(my_new_list)

# Clear is used to delete all items in the list
print("\n" + "TestList:")
my_list.clear();
print(my_list)
print(type(my_list))

