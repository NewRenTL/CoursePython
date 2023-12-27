### Dictionaries ###

my_dict = dict();
my_other_dict = {};

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Diego","Apellido":"Bustamante","Edad":20,1:"Python"}

my_dict = {
    "Name":"Diego",
    "Lastname":"Bustamante",
    "Age":35,
    "Languages":{"Python","Switf","Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Name"])
print(my_dict["Lastname"])
print(my_dict[1])

my_dict["Street"] = "Av. La Paz 500"
print(my_dict)

print("Del Street")
del my_dict["Street"]
print(my_dict)


# You can search by key or value

#Key(By default)
print("Name" in my_dict) #True (Key)
print("Diego" in my_dict) #False

print("Searchs by value or key")
#Search by Keys
print("Name" in my_dict.keys())
#Search by value
print("Diego" in my_dict.values())
print("\n")

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


print("\n")
my_list = ["Name",1,"Floor"]

my_new_dict2 = dict.fromkeys(my_list)
print(my_new_dict2)
my_new_dict2 = dict.fromkeys(("Name",1,"Floor"))
print(my_new_dict2)
my_new_dict2 = dict.fromkeys(my_dict)
print((my_new_dict2))
my_new_dict2 = dict.fromkeys(my_dict,"Diego")
print(my_new_dict2)

print("\n")

my_values =my_new_dict2.values() 
print(type(my_values))
print(list(my_values))
print(list(my_new_dict2))
print(tuple(my_new_dict2))
print(set(my_new_dict2))

