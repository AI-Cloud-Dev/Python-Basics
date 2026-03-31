# List Comprehension = Used in data processing

nums = [x*x for x in range(5)] #One line for Loop
nums1 = [x*x for x in range(9)]

# "Give me x, for every x in nums, ONLY IF x is even"
evens = [x for x in range(10) if x%2==0] #EVEN

# "Give me x, for every x in nums, ONLY IF x is odd"
odd = [x for x in range(10) if x%2!=0]

# create a new list of just Admin messages
# admin_msgs = [entry['message'] for entry in chat_history if entry['role'] == "Admin"]
# print(admin_msgs)

# Convert Strings to uppercase
str_ing = "string"
# 1. action (x.upper)
# 2. Loop(for x in string)
upper = [x.upper() for x in str_ing]
print(upper)

# Turn the list ["S", "T", "R", "I", "N", "G"] back into "HELLO"
result = "".join([x.upper() for x in str_ing]) # or
print(result)
result = str_ing.upper()
print(result)



print(nums)
print(nums1)
print(evens)
print(odd)
