# Create a file aws_topics.txt

# Each line in the file should follow this format:
# TopicName - Status
# Example:

# mathematica
# Copy code
# IAM - In Progress  
# EC2 - Completed  
# S3 - Not Started
# Write a function to:

# Add a new topic

def add_line(topic, status):
    with open("aws_topics.txt", "a") as file:
        file.write(f"{topic} - {status}\n")
        
add_line("IAM", "In Progress")
add_line("EC2", "Completed")
add_line("S3", "Not Started")
add_line("DynamoDB", "Started")


# Update the status of an existing topic
def updated_line(topic, new_status):
    with open("aws_topics.txt", "r") as file:
        lines = file.readlines()
        
        update_status = []
        for line in lines:
            if line.startswith(topic):
                update_status.append(f"{topic} - {new_status}\n")
            else:
                update_status.append(line)
    with open("aws_topics.txt", "w") as file:
        file.writelines(update_status)
updated_line("S3", "In Progress")

# List all topics with their current status
def list_topics():
    with open("aws_topics.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
list_topics()


        


                
        
        
        