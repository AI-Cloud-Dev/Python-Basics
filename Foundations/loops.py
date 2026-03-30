

# 1. Standard for loop (0 to 4)
# Note: No manual i += 1 needed; the loop handles it automatically.
print("--- Loop 1: For Loop with range ---")
for i in range(5):
    i+=1 # increament
    if(i==3):
        continue
    print(i)

# 2. While loop with manual increment
# This ensures the loop eventually ends when j reaches 5.
print("--- Loop 2: While Loop with range ---")

j= 0
while j in range(5):
    j+=1
    if(j==4):
        continue
    print(j)
    
# 3. Iterating through a list
print("\n--- Loop 3: List Iteration ---")
fruits = ["Apple", "Banana", "Cherry"]

for x in (fruits):
    print(x)

for x in (fruits):
    if x == "Banana":
        continue
    print(x)
    
# To avoid the infinite loop, we "pop" items out of the list until it's empty.
print("\n--- Loop 4: Safe While Loop with List ---")
while (fruits):
    x= fruits.pop(0)
    if x == "Apple":
        continue
    print(x)
    
names = ["Alice", "Bob", "Carol"]
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")   
    