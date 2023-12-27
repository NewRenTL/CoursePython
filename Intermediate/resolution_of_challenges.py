### Challenges ###

def operation_push_i(number):
    if(number%3 == 0 and number%5 == 0):
        print(f'{number} % 5 == 0 and {number} % 3 == 0 -> fizzbuzz')
        return "fizzbuzz"
    elif(number % 3 == 0):
        print(f'{number} % 3 == 0 -> buzz')
        return "fizz"
    elif(number % 5 == 0):
        print(f'{number} % 5 == 0 -> buzz')
        return "buzz"
    else:
        print(f'{number} pass')
        return number;
    
my_list = [operation_push_i(i) for i in range(1,101,1)]

    