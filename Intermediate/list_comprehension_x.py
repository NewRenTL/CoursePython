
my_original_list = [35,24,62,52,30,30,17]


my_list = [i for i in my_original_list]
print(my_list)

print()
my_list_numbers = [i for i in range(1,11,1)]
print(my_list_numbers)

my_range = range(8);
print()
my_list_numbers2 = [i for i in my_range]
print(my_list_numbers2)

print()
my_list_number3 = [i*i for i in my_range]
print(my_list_number3)


print()
def sum_five(number):
    return number +5;

my_list_number4 = [sum_five(i) for i in range(8)]
print(my_list_number4)