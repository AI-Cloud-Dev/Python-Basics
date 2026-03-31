# Task 1: The "Employee Profile"
# Real-Time Scenario: You are building a HR database for a single employee.

employee = {
    "id": 101, 
    "name" : "Sarah", 
    "department" : "IT" , 
    "salary" : 5000
}
print (type(employee))
employee.update({"department":"Product"})
employee["skills"] = ["Python", "SQL"]
print(employee)

# Task 2: The "Price Checker"
# Real-Time Scenario: A cashier system.

stock = {
    "Apple": 2.5,
    "Banana": 1.2,
    "Cherry": 3.0
}
stock["Banana"] +=1.5
print(stock)
if "Orange" in stock:
    print(stock["Orange"])
else: print("Out of Stock!")

print(stock.get("Orange", "Not Found"))

# Task 3: The "Database Summary"
# Real-Time Scenario: You have a list of user IDs and need to quickly see everyone's names

employee = {
    "Id": 101,
    "name": "Sree",
    "Dept": "IT",
    "salary": 5000
}
print(list(employee.keys()))
print(list(employee.values()))
for key, value in employee.items():
    print(f"Label:  {key:8} | Data: {value}")

# Task 4: The "Inventory Tracker" (Counter Logic)
# Real-Time Scenario: You are scanning items at a checkout counter. You have a list of items sold, and you need to count how many of each were bought.
sales = ["Apple", "Banana", "Apple", "Orange", "Apple", "Banana"]
inventory_count = {}
for x in sales:
    if x in inventory_count:
        inventory_count[x] +=1 #access the value using [x]
    else:
    #    inventory_count.update({x:1})
       inventory_count[x] = 1
    print(inventory_count)
print(f"Final inventory is : {inventory_count}")

# Task 5: The "Nested Database"
# Real-Time Scenario: You are managing multiple users in a single system.

users ={
    "user_01": {
        "name": "sree",
        "role":"Admin"
    },
    "user_02": {
        "name": "Raj",
        "role": "User"
    }}
print(users["user_01"])
users["user_02"].update({"role": "Superuser"})
print(users["user_02"])

# Task 6: The "Safe Login" (Input & Get)
# Real-Time Scenario: A simple login credential check.

passwords = {
    "admin": "1234",
    "guest": "0000"
}
while True:
    username = input("Enter the Username: ")
    user_password = passwords.get(username)
    # if username in passwords:
    #     x = passwords.get(username, passwords.values())
    if user_password:
        print(f"Password for {username} is: {user_password}")
    else: 
        print("User Not found")    

    repeat = input("Calculate another? y/n:").lower()
    if repeat == "n":
        print("Goodbye!")
        break        
    
    
 # ── Dicts ─────────────────────────────────────────────────
user = {"id": 1, "name": "Arjun", "roles": ["admin"]}
user["email"] = "a@b.com"         # add key
name = user.get("name", "unknown") # safe access with default
for k, v in user.items():
    print(f"{k}: {v}")