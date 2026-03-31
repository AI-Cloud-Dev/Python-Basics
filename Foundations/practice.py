# Create variables for your full profile (name, age, city, years_of_experience). Print them using one f-string with proper formatting.

name = "sree"
age = 29
city = "Chicago"
years_of_experience = 6

print(f"My name is {name}, I'm {age} of old. I lives in {city} city and I have {years_of_experience} years of experience in It Industry")


# Write a function describe_type(value) that prints the type AND whether the value is mutable or immutable.

def describe_type(value):
    val_type = type(value)
    if isinstance(value, (int, float, str, tuple, bool)):
        mutability = "Immutable"
    else: 
        mutability = "Mutable"
    print(f"Type: {val_type.__name__}, {mutability}")
    
describe_type("string")
describe_type([1,2,3,4])
describe_type({1, 2, 3})
describe_type((10.5, 6.6))
describe_type(("string", "peg"))
describe_type({1: "a", 2: "b"})
    
# Experiment: assign x = 5, then y = x, then x = 10. What is y? Why? Now do the same with a list. What happens? This is the mutable/immutable distinction in action.

x=5
y=x
x=10
print(y)

x=[5]
y=x
x.append(10)
print(y)

# FizzBuzz: print 1–100. Multiples of 3 → "Fizz", multiples of 5 → "Buzz", both → "FizzBuzz".

for n in range(100):
    if n%3==0:
        print("Fizz")
    elif n%5 ==0:
        print("Buzz")
        
# Given a list of integers, use a list comprehension to return only primes.

lst_primes = [x for x in range(50) if x > 1 and all(x % i !=0 for i in range(2, int(x**0.5)+1))]
print(lst_primes)

# Invert a dictionary (swap keys and values) using a dict comprehension.

val={"a":1, "b":2}
swap_dict= {v: k for k, v in val.items()}
print(swap_dict)
        