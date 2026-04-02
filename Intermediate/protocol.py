'''
Type System + PROTOCOLS + PYTDANTIC
'''
# Type hints : 
   
def add(a: int, b: int) -> int:
    ...
    
from typing import Protocol

# Protocal :  Duck Typing with structure 
class writer(Protocol):
    def write(self, data:str):
        self.data = data
        

# Pydantic - FASTAPI Backbone

from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    name: str
    age: int
    
"""
🧪 EXERCISES
✅ Exercise 1

Add type hints to Stack class
"""
# Last In First Out

from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    def push(self, item: T):
        self.items.append(item)
    def pop(self)-> Optional[T]:
        if self._items:
            return self._items.pop()
        return None
    def peek(self) -> Optional[T]:
        if self._items:
            return self._items[-1]
        return None
stack = Stack[int]()
stack.push(10)
stack.push(20)
print(stack.pop())
print(stack.peek())

"""
✅ Exercise 2

Create Protocol for payment system
"""
class PaymentProcessor:
    def pay(self, amount:float) -> bool:
        ...

class StripePayment:
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount} payment through Stripe")
        return True
processer: PaymentProcessor = StripePayment()
processer.pay(100.0) # Processing $100.0 payment through stripe


"""
✅ Exercise 3

Validate API input using Pydantic
"""
class UserInput(BaseModel):
    name: str
    age: int
    email: EmailStr

try:
    user = UserInput(name= "sree", age= 25, email="sree@example.com")
    print(user)
except ValidationError as e:
    print(e)

try:
    user = UserInput(name = "Bob", age = 20, email = "bob.example.com")    
except ValidationError as e:
    print("Validation Erros:")
    print(e)
    
