### Lambdas ###

sum_two_values = lambda first_value,second_value:first_value + second_value;

print(sum_two_values(2,3))

multiply_values = lambda first_value,second_value: first_value * second_value 
print(multiply_values(2,4))




# Function has a lambda function as a parameter
def sum_values(n1,function):
    return n1 + function(n1,n1);

print(sum_values(2,multiply_values))

# Function returns a lambda function return
def sum_three_values(extra):
    return lambda first_value,second_value:first_value+second_value+ extra

print(sum_three_values(5)(2,4))

