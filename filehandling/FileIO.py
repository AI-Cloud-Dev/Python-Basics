import json


# Task 1: The "Log Writer"

with open("log.txt", "w") as file:
   file.write("Entry 1: System Started\n")
   file.write( "Entry 2: User 'admin' logged in\n")
   file.write("Entry 3: Error detected at 10:00 AM\n")
   
#open and read the file after the writing/overwriting:
with open("log.txt") as f:
    print(f.read())
    
# Task 2 &3 : The "Log Reader", Reading, Filtering, and Enumerating
with open("log.txt", "r") as f:
    print("--- Part 1: Filtering for Errors ---")
    for line in f:
        print(line.strip())
        if "Error" in line:
            print(f"LOG: {line.strip()}")
            print(f"LOG: {line.rstrip()}")
    # IMPORTANT: Rewind the file to the top
    f.seek(0) 
    #If you want to track which line you are on, use enumerate()
    print("\n--- Part 2: Numbered List ---")
    for index, line in enumerate(f, start = 1): 
        print(f"Line {index}: {line.strip()}")
        
user = input("Enter the username")
    
with open("guestbook.txt", "a") as f:
    f.write(user)
        
with open("guestbook.txt", "r") as f:
    print(f.read())

        
# Task 4: The "Database Saver" (Dictionary to JSON)

data = {"last_login": "2023-10-01", "active_user": 5, "status": "Online"}

with open("config.json", "w") as f:
    json.dump(data, f, indent = 4)

print("Data successfully saved to the Config.json file")

# --- The "Database Loader" (JSON to Dictionary) ---
# Let's read it back to make sure it worked!
with open("config.json", "r") as f:
    loaded_data = json.load(f)
loaded_data["status"] = "Offline"
print(f"The updated status in new_data is: {loaded_data['status']}")
    
print(f"Loaded Data: {loaded_data}")