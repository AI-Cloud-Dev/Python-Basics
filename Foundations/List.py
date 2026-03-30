# Task 1: The "Live Tracker" (Lists)
# Real-Time Scenario: Imagine you are building a simple log for
# a security system tracking people entering a building.

vistors =[]

vistors.append("Alice")
vistors.append("Charlie")
vistors.append("Bob")

print(vistors)

vistors.remove("Alice")
print(vistors)

length = len(vistors)
print(length)

vistors.sort()
print(vistors)


# Task 2: The "Waitlist Manager"
# Real-Time Scenario: You are managing a queue for a busy restaurant.
queue = ["John", "Amy", "Rick"]
queue.insert(0, "Sarah")
queue.append("Kevin")
queue.pop(2)
print(queue)

# Task 3: The "Data Cleaner"
# Real-Time Scenario: You received a list of sensor readings, but some are errors (0) and some are duplicates.
readings = [25, 0, 32, 25, 44, 0, 100, 32]
count= 0
cleaned_readings= sorted({x for x in readings if x!=0 })
# for x in readings:
#     if x==0:
#         readings.remove(x)
    # if x==25:
    #     count+=1
print(readings)
readings.reverse()
print(readings.count(25))
print(readings)
top_three= readings[:3]
print(top_three)

# ask 4: The "Batch Processor"
# ReTal-Time Scenario: You have two separate lists of employee IDs from two different departments.

dept_a = [101, 102, 103]
dept_b = [201, 202, 203]

all_employees= dept_a

all_employees.extend(dept_b)
print(f"All employees list of dept A and B are : {all_employees}")
all_employees.extend([301, 302, 303])
print(f"All employees list with new batch: {all_employees}")
if 105 in all_employees:
    print("Employee 105 is in the list.")
else:
    print("Employee 105 was not found.")

# Task 5: The "Inventory Tracker" (Counter Logic)
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
