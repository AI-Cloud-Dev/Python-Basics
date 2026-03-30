#Task 6: The "Chat Logger" Prototype
import datetime
import json
import os

# 1. Load existing history or start fresh
if os.path.exists("chat_log.json"):
    with open("chat_log.json", "r") as f:
        chat_history = json.load(f) #Load the list
else:
    chat_history = [] #Start an empty list

#Get messages from input user
username = input("Enter the username: ")
message = input("Enter the message: ")
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_entry = {
    "user": username,
    "msg": message,
    "time": current_time
}
chat_history.append(new_entry)
print(chat_history)

#Save the WHOLE list back to the life
with open("chat_log.json", "w") as f:
    json.dump(chat_history, f, indent=4)
    
# Filter for Admin messages in the entire history
print("\n-----Admin Logs -----")

for entry in chat_history:
    if entry["user"].lower() == "admin":
        print(f"[{entry['time']}] {entry['msg']}")








# chat_history = []

# username = input("Enter the username: ")
# message = input("Enter the message: ")
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# chat_history = {
#     "user": username,
#     "message": message,
#     "time": current_time
# }

# print(chat_history)

# with open("chat_log.json", "w") as f:
#     json.dump(chat_history, f, indent=4)
    
# with open("chat_log.json", "r") as f:
#     load_data = json.load(f)
    
#     if load_data["user"].lower() == "admin":
#         print(f"ADMIN ALERT: [{load_data['time']}] {load_data['message']}")
#     else:
#         print("Log entry loaded, but user is not a admin") 