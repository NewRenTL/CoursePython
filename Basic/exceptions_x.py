### Exception Handling ###

numberOne =  5;
numberTwo =  1;
numberTwo = '1';


try:
    print(numberOne +numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred")
    
    
print()
#Try Except Else

numberTwo =  1;
try:
    print(numberOne +numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred")
else:
    #The "else" condition is executed if no error occurrs
    print("The execution continues correctly")
    

#Try Except Else Finally
print()
numberTwo =  1;
try:
    print(numberOne +numberTwo)
    print("No error has occurred")
except:
    print("An error has occurred")
else:
    #The "else" condition is executed if no error occurrs
    print("The execution continues correctly")
finally:
    # The "finally" condition is always execute 
    print("The execution continues")
 
 
 
# Exceptions by type
print()
print("Llegamos 1")

numberTwo = "1"
try:
    print(numberOne +numberTwo)
    print("No error has occurred")
except TypeError as type_Error:
    print(type_Error)
 
 
   
    
# Capture exeption information
print()
print("Llegamos 2")
numberTwo = "1"
try:
    print(numberOne +numberTwo)
    print("No error has occurred")
except ValueError as error:
    print("ValueError")
    print(error)
except TypeError as type_Error:
    print("TypeError")
    print(type_Error)
