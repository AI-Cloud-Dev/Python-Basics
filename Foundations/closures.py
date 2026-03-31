# Closures = A function that "remembers" values from its outside scope even after that scope is closed.


def make_multiplier(factor: int):
    def multiply(x: int):
        return x*factor #'factor' is captured from outer scope
    return multiply

triple = make_multiplier(3) # factor = 3
double = make_multiplier(2)
square = make_multiplier(4)
print(triple(7)) #x = 7 (3*7 = 21)
print(double(5))
print(square(5))

# Example 2 Counter
def make_counter():
    count = 0

    def increament():
        nonlocal count # because modifying the outer variable
        count+=1
        return count
    return increament
counter = make_counter()

print(counter())
print(counter())
print(counter())

# Example 3 : Logger with prefix

def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

error_log = make_logger("ERROR")
info_log = make_logger("INFO")

error_log("Something broke")
info_log("All good")

# Example 4: Private Data(Encapsulation)

# closures can act like private variables

def make_bank_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def get_balance():
        return balance
    
    return deposit, get_balance
deposit, get_balance = make_bank_account(100)

deposit(50)
print(get_balance()) # balance is hidden from outside code


def make_power(power):
    def cal_pow(num):        
        return num**power
     
    return cal_pow

square = make_power(2)
cube = make_power(3)
print(square(4))
print(cube(3))

# Task 2 Greeting generator

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}"
    return greet
    

hello = make_greeter("Hello")
bye = make_greeter("GoodBye!")
print(hello("Alice"))
print(bye("Bob"))

#Task 3: Running total
def make_accumulator():
    counter = 0
    def count_er(y):
        nonlocal counter
        counter+=y
        return counter
    return count_er

total = make_accumulator()
print(total(5))
print(total(10))

#Task 4: Simple rate limiter

def limit_calls(max_limit):
    count = 0
    def rate_limit():
        nonlocal count
        count+=1
        if count > max_limit:
            print(f"Blocked (limit of {max_limit} reached)")
        else: print(f"Allowed ({count}/{max_limit})")
        # return count
    return rate_limit

limited = limit_calls(3)
limited()
limited()
limited()
limited()
# print(limited())
# print(limited())
# print(limited())
# print(limited())
# print(limited())

