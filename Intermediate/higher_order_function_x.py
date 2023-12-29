
from functools import reduce

def sum_one(value):
    return value +1 ;

def sum_five(value):
    return value + 5;


def sum_two_values_and_add_one(first_value,second_value,function_x):
    return function_x(first_value + second_value)

print(sum_two_values_and_add_one(5,2,sum_one))
print(sum_two_values_and_add_one(5,2,sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10 ;
    return add

def sum_ten2(original_value):
    def add(value):
        return value + 10 + original_value;
    return add

add_closure = sum_ten()

print(add_closure(10))

add_closure = sum_ten2(10)

print(add_closure(10))


print(sum_ten2(10)(10))


print()
### Built-in Higher Order Functions ###



def multiply_two(number):
    return number*2;

numbers = [2,5,10,21]
#Map

print(list(map(multiply_two,numbers)))
print(list(map(lambda number:number*2,numbers)))

#Filter

def filter_greater_than_ten(number):
    return number > 10;

print(list(filter(filter_greater_than_ten,numbers)))
print(list(filter(lambda number:number>10,numbers)))

#Reduce

def sum_two_values_1(first_value,second_value):
    return first_value + second_value;

print(reduce(sum_two_values_1,numbers))
