
# Variables
name = "Sree"
age = 25

# Data Types - int, string, List, Dict 
print(type(name))
print(type(age))

# Conditions
if name == "Sree":
    print(f"{name} is {age}" )
else: print(f"{name} is not {age}")

# elif
if age < 15:
    print(f"{name} is Child with age {age}")
elif age <20:
    print(f"{name} is Teenager with age {age}")
else: print(f"{name} is Adult with age {age}")

# Loops
i=0
for i in range(5):
    print(i)
    
# While Loop
j=0
while j<6:
    j+=1 # iterate and increament
    if j==3:
        continue
    print(i)

# Functions
def greet(name):
    return name

def greetings(name):
    message = f"Warm Greetings to {name}"
    print(message)
greetings("Pop")

def test():
    print("testing")
    
test()
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()

# Arrays

# List

# Tuples

# Dict

# File Handling



# Basic OOPs