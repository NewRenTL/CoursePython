### File Handling ###


# .txt file
import os

#Read "r"
#Write "w"
def lines_separated():
    print("--------------------------------")
#Open function read from the root directory
my_txt_file1 = open(".\\Intermediate\\my_file.txt","r+")

'''
file = open("filename.txt", "r")  # "r" mode for reading
file = open("filename.txt", "w")  # "w" mode for writing (creates a new file or overwriting an existing one)
file = open("filename.txt", "a")  # "a" mode to add the file to add content to the end)
file = open("filename.txt", "r+")  # "r+" mode for reading and writing
'''

#print(my_txt_file1.read())
print()

## Read(number parameter) function reads a specific number of characters in the file 

print(my_txt_file1.read(10)) 

lines_separated()

print(my_txt_file1.read(12)) 

lines_separated()

my_txt_file1 = open(".\\Intermediate\\my_file.txt","r+")

#Read Line
print(my_txt_file1.readline(),end="")
print(my_txt_file1.readline(),end="")
#Read Lines method returns a list of remaining sentences 
print(my_txt_file1.readlines())

lines_separated()
my_txt_file1 = open(".\\Intermediate\\my_file.txt","r+")
for line in my_txt_file1:
    print(line,end="")
print()
my_txt_file1.close()
lines_separated()
print("Write a new file <--")
my_txt_file2 = open(".\\Intermediate\\my_file2.txt","w+")

my_txt_file2.write("My name is Diego\nMy surname is Bustamante\nI'm 35 years old\nand my preferred language is Python");

 # Seek Method positions the pointer in the file, 
 # seek(0) positions at the beginning of the file
 # seek(offset,whence) "whence" parameter can take value 0,1,2 
 # whence == 0 positions the pointer at the beginning of the file
 # whence == 1 positions the pointer at the current position
 # whence == 2 positions the pointer at the final position of the file
 # offset It is the number of bytes to move the pointer

 # my_txt_file2.seek(0,2)
my_txt_file2.write("\nAlthough I also like Kotlin") 

my_txt_file2.seek(0,0);

for line in my_txt_file2.readlines():
    print(line,end="")
print()

my_txt_file2.close()

#How I can remove a file?
#Note:Before deleting a file you must terminate pending processes with the file
os.remove("Intermediate/my_file2.txt")


#JSON File

lines_separated()
import json
print("WRITE JSON FILE")
json_file = open("Intermediate/my_file.json","w+"); #Open a new json file

json_test = {
    "name":"Diego",
    "surname":"Bustamante",
    "age":20,
    "language":["Swift","Python","C++"],
    "website":"https://www.google.com"
}

# json.dump method allows me to save a dictionary inside a json file
json.dump(json_test,json_file,indent=4)

json_file.close()

with open("./Intermediate/my_file.json","r") as my_other_file_json:
    for line in my_other_file_json:
        print(line)

lines_separated()

# How I can load a json file inside a variable?
print("LOAD JSON FILE:");

json_dict1 = json.load(open("Intermediate/my_file.json"))
print(type(json_dict1))
print(json_dict1)

lines_separated();

#.csv file
import csv

print("WRITE CSV <--")
with open("Intermediate/my_file.csv", "w+", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["name", "surname", "age", "language", "website"])
    csv_writer.writerow(["Diego", "Bustamante", 20, "Python", "https://www.google.com"])

print("READ CSV <--")
with open("Intermediate/my_file.csv", "r", newline="") as csv_file_x:
    csv_reader = csv.reader(csv_file_x, delimiter=",")
    for row in csv_reader:
        for value in row:
            print(value,end=",")
        print()

import xml
