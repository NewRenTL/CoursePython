### Sets ###

my_set  = set();
my_other_set = {};

print(type(my_set))
print(type(my_other_set)) #Initially it is a dictionary


my_other_set = {"Brais","Moure",35}

print(type(my_other_set))

# I'm here printing the length of the "set"
print(len(my_other_set))

my_other_set.add("Sierpe")

# A set isn't an  ordenered structure
print(my_other_set)

# A set hasn't repeated list elements
my_other_set.add("Sierpe")
print(my_other_set)

#A set uses a hash for its data structure, so we can't access a specific element

# Is there an element in the set?
print ("Moure" in my_other_set) #True
print ("Mouri" in my_other_set) #False

my_other_set.remove("Moure")
print(my_other_set)

#Update method updates this set with the union of itself and set parameter
my_other_set.update({"Holamundo","Sierpe"})
print(my_other_set)


#Clear method
my_other_set.clear();
print(my_other_set)
print(len(my_other_set))

del my_other_set

my_set = {"Brais","Moure",35}
my_list = list(my_set);
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin","Switf","Python"}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set).union(my_set).union({"Javascript","C#"}))


# Difference method returns a new set with elements within the itself set but not in others
print(my_new_set)
print(my_new_set.difference({"Kotlin","C#"}))