### Functions ###

def my_funtion1():
    print("This is a function")
    

def sum_two_values(first_number:int,second_number:int):
    print(first_number + second_number)
    
def sum_two_values_with_return(first_number:int,second_number:int):
    return first_number + second_number
    
#sum_two_values(1,2)
#sum_two_values("Hola","Mundo")

#my_result = sum_two_values_with_return(2,4)
#print(my_result)

def print_name(name:str,surname:str):
    print(f'{name} {surname}')
    
#print_name(surname="Bustamante",name="Diego")

def print_name_with_default(name:str,surname:str,alias = "No alias"):
    print(f'{name} {surname} {alias}')

#print_name_with_default("Diego","Bustamante")
#print_name_with_default("Diego","Bustamante","Software Engineer")

