def save_study_progress(day, topic, hours):
    # append - a
    with open("study_log.txt", "a") as file:
        file.write(f"Day {day} - {topic} - {hours} hours\n")
save_study_progress(1, "ErrorHandling", 5)
save_study_progress(2, "FileHandling", 8)
save_study_progress(3, "JsonHandling", 6)

def calculate():
    total_days = 0
    total_hours = 0
    with open("study_log.txt", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            print(repr(line))
        
        for line in lines:
            parts = line.strip().split(" - ")
            print("Debug: Split parts:", parts)
            
            if len(parts) == 3 and "hours" in parts[2]:
                hours = int(parts[2].split()[0])
                total_hours += hours
                total_days += 1
    print(f"Total days logged: {total_days}")
    print(f"Total hours studied: {total_hours}")
    
calculate()
# Clear the file (optional, for testing)
# open("study_log.txt", "w").close()
            
        