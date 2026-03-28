# JSON Handling, Error Handling, Requests(API), Virtual env+lib

# Json Handling
# Task 1
import json
dict = {
    "goals": "AWS Dev",
    "tools": ["EC2", "S3", "EKS"],
    "hours": 8
}
# convert dict to json
json_str = json.dumps(dict)
print("Json String is :", json_str)
# convert back to dict from json
parsed_dict = json.loads(json_str)
# printing one nested value
print("parsed dict:", parsed_dict["tools"])

# Task 2
json_user= '''
{
  "users": [
    {"name": "Alice", "certified": true, "hours": 6},
    {"name": "Bob", "certified": false, "hours": 4},
    {"name": "Sree", "certified": true, "hours": 8}
  ]
}
'''
# convert json str to python object
parsed_user = json.loads(json_user)
for user in parsed_user["users"]:
    if user["certified"] == True and user["hours"] >= 6:
        print(user["name"])

# Task 3
json_event='''
{
  "event": "new_signup",
  "user_info": {
    "username": "sree_user",
    "email": "sree@example.com",
    "region": "us-west-2",
    "preferences": {
      "notifications": true,
      "newsletter": false
    }
  }
}
'''
parsed_event = json.loads(json_event)

# extract values
name = parsed_event["user_info"]["username"] 
email =parsed_event["user_info"]["email"]
region = parsed_event["user_info"]["region"]
notify= parsed_event["user_info"]["preferences"]["notifications"]

# converting boolean to string
notify_status = "Enabled" if notify else "Disabled"

# converting notification boolean to string
notify = str(parsed_event["user_info"]["preferences"]["notifications"]) 
    
print(f"New signup: {name} from {region}(Email: {email}) - Notifications: {notify_status}")

# Join values with a separator (e.g., comma)
joined_string = ",".join([name, email, region, notify])
print(f"Joined string is:", joined_string)

    

# task 4

# Add a "status": "active" field inside user_info
parsed_event["user_info"]["status"]="active"

# convert the updated dictionary back to JSON using json.dumps() 
updatedict = json.dumps(parsed_event)
print(updatedict)
print(json.dumps(parsed_event, indent=2))


