# File I/O

# Even though your Python script and test.txt are both in the same folder (Day2), Python doesn't always run from the script’s directory.

# 💡 Python reads files relative to the current working directory (CWD) — not the script’s location unless you explicitly set it.
# print(os.getcwd())


        #*****they are 3 ways to retrieve the file. ****
                #   *********1 Way*************
# import os

# Change to the directory of the script
# os.chdir(os.path.dirname(__file__))
# with open("test.txt", "r") as file:

                #   *********2 Way*************
                
#Use __file__ and os.path to build absolute path
# file_path = os.path.join(os.path.dirname(__file__), "test.txt")
# with open(file_path, "r") as file:

                #   *********3 Way*************
                
# Use full or raw path
# with open(r"Desktop\Visualstudio\Python25\Day2\test.txt", "r") as file:


# write to a file
with open("aws_goals.txt", 'w') as file:
    file.write("Learn Lambda\nMaster s3\nExplore SageMaker")


# read from a file
with open("test.txt", 'r') as file:
    content= file.read()
    print("your goals:\n", content)
    

# reverse the string/content from the file
reversed_test = content[::-1]

# write reversed string/content to a new file
with open("reversed_test.txt", "w") as file:
    file.write(reversed_test)

# Reverse by lines(Last line becomes first)

with open("test.txt","r") as file:
    lines = file.readlines()
    
# reverse the list of lines
reversed_line = lines[::-1]

# write to a new file
with open("reverse_lines.txt", "w") as file:
    file.writelines(reversed_line)
    
    