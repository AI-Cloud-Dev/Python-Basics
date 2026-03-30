import json
import datetime
import os

FILE_NAME = "chat_history.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        chat_history=json.load(f)
else:
    chat_history=[]


def save_message(new_entry):  
    chat_history.append(new_entry)
        
    with open(FILE_NAME, "w") as f:
        json.dump(chat_history, f, indent = 4)        
    print("\n--- Message Saved Successfully")

def read_message():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                load_data= json.load(f)
                for entry in load_data:
                    print(f"{entry['user']} ({entry['role']}) [{entry['current_time']}]: {entry['message']}")
                return load_data
        except json.JSONDecodeError:
            print("File corrupted, starting Fresh.")
            return []
    else:
        print(f"\nFile with filename {FILE_NAME} found yet.")
    
while True:
    print("1. Add Message")
    print("2. view Message")
    print("3. Exit")
    
    choice =input("Choose: ")
    if choice == "1":
        user = input("Enter the username: ")
        message  = input("Enter your Message: ")
        role = input("Enter the role: ")
        
        new_entry={
                "user": user,
                "message": message,
                "role": role,
                "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }  
        save_message(new_entry)
        
    elif choice == "2":
        read_message()
    elif choice == "3":
        print("GoodBye!")
        break
    else:
        print("Invalid choice, please try again")
    
    # repeat= input("Continue? y/n").lower()
    # if repeat == "n":
    #     print("GoodBye!")
    #     break   

  