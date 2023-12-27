

print("While Loop:")
my_condition = 0;

while my_condition < 10:
    print(my_condition,end=" ")
    my_condition += 1
else: ##This is optional
    print("\nMy condition is greater or equal to 10")
    

while my_condition < 20:
    
    if my_condition == 15:
        print("Stop the execution")
        break;
    print(my_condition,end=" ")
    my_condition+=1;


my_list = [35,24,62,52,30,30,17]

print("For Loop:")
print("List-")
for element in my_list:
    print(element,end=" ")

print("\n")
print("Tuple-")
my_tuple = (20,1.70,"Diego","Bustamante")
for element in my_tuple:
    print(element,end=" ")

print("Set-")
my_set = {"Diego","Bustamante",20}
for element in my_set:
    print(element,end=" ")


print("\n")
print("Dictionary-")
my_dict = {
    "Name":"Diego",
    "Lastname":"Bustamante",
    "Age":35,
    "Languages":{"Python","Switf","Kotlin"},
    1:1.77
    }


#By default (keys)
for element in my_dict:
    print(element,end=" ")
print("\n")
#By keys especifically
for key in my_dict.keys():
    print(key,end=" ")
print("\n")
#By values especifically
for values in my_dict.values():
    print(values,end=" ")
print("\n")

#For within the values in my dictionary
for values in my_dict.values():
    print(values,end=" ")
print("\n")



