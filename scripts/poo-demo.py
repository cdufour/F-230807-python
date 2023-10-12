class Student:
    # propriétés
    age = 0
    firstname = ""

    # méthodes

    # constructeur
    # arguments obligatoire (required) à placer avant les arguments optionnels
    def __init__(self, firstname, age=0):
        self.age = age
        self.firstname = firstname

    def get_age(self):
        return self.age
    
    def get_firstname(self):
        return self.firstname
    
    def set_age(self, age):
        self.age = age

    def is_major(self):
        return self.age >= 18
    

# instanciation
s1 = Student("Alessandro", 18)
s2 = Student("Ivan", 36)
s3 = Student("Toto", 14)

s1.set_age(45)

print(s1.get_age())
print(s2.get_age())

if s1.is_major():
    print(f"{s1.get_firstname()} est majeur")

if not s3.is_major():
    print(f"{s3.get_firstname()} n'est pas majeur")