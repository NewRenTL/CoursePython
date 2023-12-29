### Challenges ###

#1
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
    
#my_list = [operation_push_i(i) for i in range(1,101,1)]

#2
def is_Anagram(word_one,word_two):
    if word_one.lower() == word_two.lower():
        return False;
    return sorted(word_two.lower()) == sorted(word_one.lower())

#print(is_Anagram("Amor","Roma"))


#3
#Fibonacci

def fibonacci2(n):#2
    if n < 0:
        return "Your input must be positive"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


def fibonacci():
    prev = 0;
    next = 1;
    for i in range(0,51):
        print(f'{i}:{prev}')
        fib = prev + next;
        prev = next;
        next = fib
        
#fibonacci()

'''
for _ in range(0,51):
    if(_ < 0):
        break
    print(f'{_}:{fibonacci2(_)}')
'''

#Prime Number

def is_Prime(number):
    
    if(number <= 1):
        return False;
    
    for _ in range(2,int(number**0.5)+1):
        if(number % _ == 0):
            return False
    return True;

'''
for i in range(1,15):
    if(is_Prime(i)):
        print(f'{i}')
'''
     
# Reverse

def reverse1(text):
    reversed_text = list(text)  # Convert a string to a list of characters
    for i in range(0, len(reversed_text)//2):
        temp = reversed_text[len(reversed_text)-1 - i]  # Save the final character
        reversed_text[len(reversed_text)-1 - i] = reversed_text[i]  # Assigns the initial character to the end
        reversed_text[i] = temp  # Assigns to the saved character at the beginning
    return ''.join(reversed_text)

def reverse2(text):
    return text[::-1]

#print(reverse1("Hello"))
#print(reverse2("Hello"))


