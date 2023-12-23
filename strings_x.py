myString1 = "My string";
my_other_String1 = "Other string";


print(len(myString1));
print(len(my_other_String1))

print(myString1 + " " + my_other_String1)

my_new_line_string = "This is a String\n with a line break"
print(my_new_line_string);

my_tab_string = "\tThis is a string with tab"
print(my_tab_string)

my_scape_string = "\\t This is a scape \\n string"
print(my_scape_string)

# Formatting
print("\n")
name,surname,age = "Diego","Bustamante",20;

print("My name is {} {} and I'm {} years old".format(name,surname,age))
print("My name is %s %s and I'm %s years old"%(name,surname,age))
print("My name is "+name+ " " + surname+ " and I'm "+str(age)+" years old")


language =  "Python";
a,b,c,d,e,f = language

print(a,b,c,d,e,f)

#String Division
language_slice = language[1:3];# [1:3>
print(language_slice)

language_slice = language[1:]; # [1:end]
print(language_slice)

language_slice = language[-2]; # [1:end]
print(language_slice)


language_slice = language[0:6:2]
print(language_slice)
#Reverse string

reversed_language = language[::-1]
print(reversed_language)

#Capitalize

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.isascii())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
    

