from typing import ClassVar
from dataclasses import dataclass, field

class BankAccount:
    # class variable - shared by All instances
    interest_rate: ClassVar[float]
    
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance # _ prefix = "private by convention"
    
    # Property - getter/setter as attribute
    
    @property
    def balance(self) -> float:
        return self.balance
    
    @balance.setter
    def balance(self, v: float):
          if v < 0: raise ValueError("Balance cannot be Negative")
          self.balance = v
    
    def deposit(self, amount : float):
        self.balance += amount
        return self # method chaining
    
    #Magic methods(dunder)
    def __repr__(self) -> str:
        return f"BankAccount(owner = {self.owner}, balance = {self.balance})"
    
    def __add__(self, other: "BankAccount"):
        #Merge Two Accounts
        return BankAccount(f"{self.owner}+{other.owner}",
                           self.balance + other.balance)
        
    def __lt__(self, other):
        return self.balance < other.balance
    
    
# Inheritance
    
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float):
        super().__init__(owner, balance)
        self.interest_rate = 0.05 # Override class var
        
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)
        return self 
    
# DataClass (modern, cleaner OOP)

@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory = list)
    
    def discounted(self, pct: float) -> float:
        return self.price*(1-pct)    