def subjects(day, subject, hours):
    with open("study_stats.csv", "a") as file:
        file.write(f"Day {day}, {subject}, {hours}\n")

subjects(1, "AWS", 6)
subjects(2, "Python", 8)
subjects(3, "Javascript", 5)
subjects(4, "NodeJs", 3)
subjects(5, "AWS", 8)
subjects(6, "Python", 10)

def calculate(subject):
    total_hours = 0
    with open("study_stats.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            if subject in line:
                parts = line.strip().split(",")
                total_hours += int(parts[2].strip())
    print(f"{total_hours}")
calculate("AWS")