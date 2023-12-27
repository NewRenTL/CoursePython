### Tuples

my_tuple = tuple();
my_other_tuple = ();

my_tuple = (35,1.77,"Brais","Moure")
my_other_tuple = (35,60,30)
print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) error out of index
#print(my_tuple[-6])

# A tuple only has one2 operations (count() and index())

print(my_tuple.index("Brais"))
print(my_tuple.count("Moure"))

# But I can't change a value within the tuple
# my_tuple[0] = 20; Error

print("\n")

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)

my_tuple[3] = "Sierpe"
my_tuple.insert(1,"Red")
print(my_tuple)

my_tuple = tuple(my_tuple);
print(type(my_tuple))
print(my_tuple)

del my_tuple


