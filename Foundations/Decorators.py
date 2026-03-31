# Decorators is a function that takes another function and adds some behavior to return a new function
#  Closure applied to functions

import time, functools


def my_decoration(func):
    def wrapper():
        print("Before")
        func()
        # def say_hello():
        #     print("Hello")
        print("After")
    return wrapper

def say_hello():
    print("Hello!")
# No @  
say_hello = my_decoration(say_hello)
say_hello()


# @ syntax

@my_decoration
def say_hello():
    print("Hello!")
say_hello()

# Logging Decorator

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a+b

print(add(2,3))

# Timing Decorator

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end-start}")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()

# Authorization check

def require_admin(func):
    def wrapper(user):
        if user != "admin":
            return "Access Denied"
        return func(user)
    return wrapper

@require_admin
def delete_data(user):
    return "Data deleted"

print(delete_data("admin"))
print(delete_data("guest"))

# 
def decorator(func):
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

# ── Decorators (closures applied to functions) ────────────
import time, functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(0.1)

slow_task()   # slow_task took 0.1001s

# Decorators with arguments

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
              result = func(*args, **kwargs)
              return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")
greet()
            
# Bad decorator forgetting return 
def bad_decorator(func):
    def wrapper():
        func()   # forgot return
    return wrapper


# Task 1 print before/after

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished...")
        return result
    return wrapper

@decorator
def create():
    return
create()

# Task 2 Double result

def double_result(func):
    def wrapper(*args, **kwargs):        
        return 2* func(*args, **kwargs)
    return wrapper

@double_result
def add(a, b):
    return a + b
print(add(2, 3))

# task 3 Count calls

def decorator(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls+=1
        print(f"call #{calls}")
        return func(*args, **kwargs)
        
    return wrapper

@decorator
def count():
    return 
count()
count()
count()

# Task 4: Only allow Positive numbers
def positive(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if n < 0:
                print("Invalid")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@positive(-1)
def posti_ve():
    return
posti_ve()
                 

