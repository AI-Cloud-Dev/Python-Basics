'''
Generators = Lazy data machine

Instead of storing everything -> generate when needed

Used in Streaming data, large datasets, AI pipelines
'''

def count_up(n):
    for i in range(n):
        yield i
        print(i)
        
gen = count_up(9)
print(gen)

def fibonacci(n):
    ''' Generate first n Fibonacci numbers lazily'''
    a, b = 0, 1
    for _ in range(n):
        yield a # pause and return current number
        a, b =b, a + b #update for next 
#Example usage
for num in fibonacci(10):
    print(num)
    
# Read file line by line
# with open() and iterating
with open("config.json", "r") as f:
    for line in f: # iterates line by line, lazy reading
        line = line.strip() # remove newline characters -> \n or extra spaces
        print(line)
        
# readline() in a loop
file = open("config.json", "r")
while True:
    line = file.readline()
    if not line: #End of Line
        break
    print(line.strip())
file.close()

# Infinite count generator

def infinite_count(start=0):
    n = start
    while True:   #Infinite Loop
        yield n   #produce current number
        n +=1     #increament for next
        
#Example usage
counter = infinite_count(5)
for _ in range(10):
    print(next(counter))
    