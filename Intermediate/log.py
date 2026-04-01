'''
Logging = writing what yor program is doing into file or console

Think - your app is a robot and logging is its dairy

Logging helps trace execution and debug production issues without stopping the system.
'''
# Basic logging

import logging

# logging.basicConfig(level = logging.INFO)

# logging.info("App strated")
# logging.warning("This is a warning!")
# logging.error("Something failed")
logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )

def log_action(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished: {func.__name__}")
        return result
    return wrapper

# Task 1

class App:
    @log_action
    def __init__(self, name):
        self.name = name
        # logging.info("Program started")

    def login(self):
        try:
            user_input= int(input("Enter the Pin: "))
            # logging.info(f"User Input: {user_input}")
        except ValueError as e:
            # logging.error("Invalid credentials")     
            print(f"{e}")  
       
    def shutdown(self):
        # logging.info(f"----{self.name} Program end")
        return 
        
my_app = App("chatsystem")
my_app.login()
my_app.shutdown()

# Task 2

class Stack:
    
    def __init__(self, items=None):
        if items is None:
            self.items=[]
        else:
            self.items = list(items)
        # logging.info("Stack strted")
    @log_action
    def push(self, item):
        self.items.append(item)
        # logging.info(f"Pushed {item}")
    def is_empty(self):
        return len(self.items)==0
    @log_action
    def pop(self):
        try:
            if self.is_empty(): # Added ()
                logging.error("Attempted to pop from empty stack!")
        except IndexError as e:
            raise IndexError(f"Stack is Empty {e}")
        item = self.items.pop()
        # logging.info(f"Popped {item}")
        return item
    def __len__(self):
        return len(self.items)
    def __str__(self):
        # This makes print(s) look like a real list
        return f"Stack currently holds: {self.items}"

s= Stack()

s.push(10)
s.push(20)
s.pop()
print(s.is_empty())
print(len(s))
print(s)

print(s.pop())


#Task 3

class divide:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    @log_action
    def div(self):
        try:
            if self.num2 != 0:
                result= self.num1/self.num2
                logging.info(f"{self.num1} divided by {self.num2} with the result {result}")
                return result
        except ZeroDivisionError:
            logging.error(f"{self.num2} is Zero")
            return None
        
    
d=divide(20, 40)

print(d.div())
d= divide(20, 0)
print(d.div())

# Logging with decorators

# def log_action(func):
#     def wrapper(*args, **kwargs):
#         logging.info(f"Executing: {func.__name__}")
#         result = func(*args, **kwargs)
#         logging.info(f"Finished: {func.__name__}")
#         return result
#     return wrapper

class SimpleMath:
    @log_action # this wraps the add function automatically
    
    def add(self, a, b):
        return a+b
math_bot = SimpleMath()
print(math_bot.add(5, 10))
    

            
