
class Person:
    def __init__ (self,name,surname,alias = "No alias"):
        self.name = name;
        self.surname = surname;
    def walk(self):
        print(f'{self.name} {self.surname} is walking')

my_person1 = Person("Diego","Bustamante")
print(my_person1.name)
print(my_person1.surname)
print(f'{my_person1.name} {my_person1.surname}')
my_person1.walk()


my_person2 = Person("Diana","Monjaras","Accounting")

my_person2.walk()
my_person2.surname = "Bustamante"
print(my_person2.surname)