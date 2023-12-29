### Regular Expressions ###

def separated_lines():
    print("-"*20)

import re

my_string = "This is my lesson number 7: Regular Expressions"
my_other_string = "This is not my lesson number 6: File management"

separated_lines()
print("MATCH 1:")
match1 = re.match("This is my lesson",my_string,re.I);
print(type(match1))
start1,end1  = match1.span()

print(match1.span())
print(start1,end1)
print(my_string[start1:end1])

separated_lines()
print("MATCH 2:")

match2 = re.match("This is my lesson",my_other_string)

if(match2):
    test_match = lambda test_match: ("There is" if test_match else "There is no")
    start2,end2  = match2.span()
    print(match2.span())
    print(start2,end2)
    print(my_string[start2:end2])
    print(test_match(match2))
else:
    print("Doesn't exists")


separated_lines()
# Search
print("SEARCH 1:")
search1 = re.search("lesson",my_string,re.I)
print(search1)
start3,end3 = search1.span()
print(my_string[start3:end3])


#FindAll
separated_lines()
print("FINDALL 1:")
findall1 = re.findall("lesson",my_string,re.I)
print(findall1)

#Split
separated_lines()
print("SPLIT1:")
my_string2 = "Hello\nWorld\nDiego"
split1 = re.split("\n",my_string2)
print(split1)

#Sub
separated_lines()
my_string3 ="My lesson1 Lesson2 Diego"
print("SUB:")
print(re.sub("lesson","LESSON",my_string))
print(re.sub("lesson|Lesson","LESSON",my_string3))

# Patterns
separated_lines()
print("Patterns")

my_string4 ="My lesson1 Lesson2 Diego diego"
pattern1 = r"[lL]esson|[Dd]iego"
print(re.findall(pattern1,my_string4))
pattern2 = r"[a-zA-z]"
print(re.findall(pattern2,my_string4))
pattern3 = r"[0-9]"
print(re.findall(pattern3,my_string4))
print(re.search(pattern3,my_string4))
pattern4 = r"\d"
print(re.findall(pattern4,my_string4))

email = "diego.bustamante@utec.edu.pe"
pattern_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern_email,email))
