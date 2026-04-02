'''
Memory Efficient Patterns : Don't load everything into memory
Techniques : Generators instead of lists, iterators, Chunk Processing
'''
import time
from datetime import datetime
import random
import asyncio
# Process 1M numbers using generator


# Bad - Memory heavy
''' Stores 1M numbers in memory
    then stores another 1M squares
    High memory usage (~tens of MB)
'''
nums = [i for i in range(1_00_000)] # reates full list in memory
squares = [x * x for x in nums]
print(sum(squares))

# Good - Generator , Memory efficient
def generate_numbers(n):
    for i in range(n):
        yield i
        
def process_numbers():
    total = 0
    for num in generate_numbers(1_000_000):
        total += num *num
    return total
print(process_numbers())

# even better (Generator expression) Memory usage = constant(O(1))
total = sum(x * x for x in range(1_000_000)) # does not create a list, produces values one at a time
print(total)


'''
Real world pattern 
this pattern is used in - Log processing (million of lines)
                          Streaming APIs
                          Data pipelines(ETL)
                          AI preprocessing
useful when you want batch processing
avoid both huge memory + too many tiny operations
'''
# Bonus : Chunk processing (advanced pattern)

def chunked_generator(n, chunk_size=1000000):
    for i in range(0, n, chunk_size):
        yield range(i, min(i + chunk_size, n))
        
for chunk in chunked_generator(1_000_000):
    for num in chunk:
        pass #process here

# Exercise 3 - Simulate Streaming logs
''' Create a system where logs are generated continuously (like a stream) and processed one by one.
   what generate logs : generator
   what proces logs : loop/consumer
'''

def log_stream():
    levels = ["INFO", "ERROR", "DEBUG"]
    counter = 1
    while True:
        # create a log string with a timestamp and increament ID
        timestamp = datetime.now().strftime("%H:%M:%S")
        level = random.choice(levels)
        # Step 4: Yield the log
        yield f"[{timestamp}] ID:{counter} - {level}: System operating... "
        counter +=1
        time.sleep(1)
# --- Step 3: Consume the logs ---
print("----starting log stream")

# Intialize the generator
generator = log_stream()

# Take first 10 logs
for _ in range(10):
    log_entry = next(generator)
    
    # Optional upgrade: Filter for Errors only
    if "ERROR" in log_entry:
        print(f" ALERT: {log_entry}")
    else:
        print(log_entry)
print("----stream Paused")
    

# Exercise 4 : Generator + File Reading + Async
""" Process a file line by line asynchronously"""


def read_file_lazy(filename):
    with open("config.json", "r") as f:
        for line in f:
            yield line 
async def process_line(line):
    await asyncio.sleep(1)
    print(f"the processing line: {line}")
async def main():
    # await asyncio.gather(read_file_lazy(), process_line())
    tasks= []
    for line in read_file_lazy("config.json"):
        tasks.append(process_line(line.strip()))
    await asyncio.gather(*tasks)
asyncio.run(main())
         

        
        

    