# variables
name = "sree"
role = "AWS Developer"
hours = 7
certified = True
print(type(name))
print(type(role))
print(type(hours))
print(type(certified))

# Lists
aws_services = ["EC2", "S3", "Lambda","EKS","VPC"]
aws_services.append("DynoDB")
aws_services.append("Fargate")
aws_services.remove("VPC")
print(aws_services)

# Dictionary
diction = {
    "name": "sree",
    "goal": "AWS dev",
    "hours": 7,
    "certified": True,
    "languages": ["python", "Javascript", "NodeJs"]
}
print(diction)
print(diction["certified"])
print(diction.get("hours"))

# Control Flow - If/Else
study_hours = 8
if study_hours >= 6:
    print("On Track")
elif 4<= study_hours > 6:
    print("Almost There")
else:
    print("Needs Improvement");
    
# Loops
for service in aws_services:
    print(f"Mastering {service} with Python")
    
# Functions
def calculate_total_study(hours_per_day, days):
    return hours_per_day*days
print(calculate_total_study(8, 30))

# dict + function
def user_description(diction):
    return f"{diction['name']} is learning {', '.join(diction['languages'])} to become a {diction['goal']}."
print(user_description(diction))


