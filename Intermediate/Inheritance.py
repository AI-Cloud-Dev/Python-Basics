
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
        
p1 = Person("Sree", 23)
p1.greet()

class Dog:
    species = "Animal" #class property
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")
d1 = Dog("Buddy", 3)
print(d1.name)
print(d1.age)
del d1.age
d1.bark()
print(d1.species)
d1.species = "Golden Retreiever"
print(d1.species)
d1.breed = "Husky" #update /add
d1.age = 4
print(d1.age)
print(d1.breed)


# Inheritance
class Animal:
    def __init__(self, name):
        self.name =name
    def speak(self):
        print(self.name)

class Dog(Animal):
    pass

d1 = Dog("Rex")
d1.speak()

class User:
    def __init__(self, username):
        self.username = username
        self.is_logged_in = False
    def login(self):
        self.is_logged_in = True
        print(f"User {self.username} has logged in")
        return self

class Admin(User):
    def __init__(self, username, permissions):
        super().__init__(username)
        self.permisssions = permissions
    def delete_user(self, target_user):
        if "delete" in self.permisssions:
            print(f"Admin {self.username} deleted {target_user}")
        else:
            print("Access Denied: No delete permission")
            

# Test Logic
member = User("Sree")
member.login()

# Create an admin with special powers
boss = Admin("Raj", ["delete", "edit"])
boss.login()
boss.delete_user("Guest123") #Extra Admin power