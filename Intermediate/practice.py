# Task 1: Build a Stack class using a list internally. Implement push, pop, peek, is_empty, __len__, __repr__.
'''
stack = you can add on top(PUSH), remove from top(POP) and look at top(PEEK)
This is called LIFO - Last In, First Out
'''
from dataclasses import dataclass, field

class stack:
    def __init__(self, items=None):
        # Using None as a default prevents the "mutable Trap"
        if items is None:
            self.items = []
        else:
            self.items = list(items)
            
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        Last_item = self.items[-1]
        return Last_item
    def is_empty(self):
        return len(self.items) == 0
    def __len__(self):
        return len(self.items)
    def __repr__(self):
        return f"Stack({self.items})"
    
s = stack()

s.push(30)
s.push(20)
s.push(10)

print(s)
print(s.peek())
print(s.pop())
print(len(s)) 
print(s.is_empty())


#Task 2 Build a Temperature dataclass that stores in Celsius. Add properties for Fahrenheit and Kelvin conversion.

@dataclass
class Temperature:
    celsius: float
    
    def fahrenheit(self):
        return (self.celsius*9/5) + 32
    
    def kelvin(self):
        return (self.celsius + 273.5)
    
t= Temperature(32)

print(t.fahrenheit())
print(t.kelvin())
    

#Task 3: Implement __contains__ for a custom NumberRange class so 5 in NumberRange(1, 10) works.
# Is 5 inside this range => 5 in range/object 
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __contains__(self, target):
        return self.start <= target >= self.end

range = NumberRange(1, 10)
print(6 in range)
print(11 in range)
            
 