'''
Async - Doing multiple tasks without waiting
Async improves performance by handling I/O bound tasks concurrently

Normal Sync - you cook -> wait -> eat -> wash
Async - you cook -> while cooking ->  you wash the dishes : which is faster
'''

# Basic Async Code

import asyncio, time, random # async engine

async def say_hello(): # defines async function
    print("Hello")
    await asyncio.sleep(1) #wait without blocking
    print("World")

asyncio.run(say_hello())

# Multiple tasks
async def task1():
    await asyncio.sleep(1)
    print("Task1 done")
async def task2():
    await asyncio.sleep(1)
    print("Task2 done")
async def task3():
    await asyncio.sleep(1)
    print("Task3 done")
async def main():
    await asyncio.gather(task1(), task2(), task3())
    
asyncio.run(main())

# Task 1

async def test():
    print("Start")
    await asyncio.sleep(2)
    print("End")
async def main():
    await asyncio.gather(test())

asyncio.run(main())

# Task 2

async def test1():
    await asyncio.sleep(2)
    print("Test 1 completion")
async def test2():
    await asyncio.sleep(3)
    print("Test 2 completion")
async def main():
    await asyncio.gather(test1(), test2())

asyncio.run(main())

# Task  3 - run multiple calls at the same time(concurrently)

async def fetch_data(task_id):
    print(f"Task {task_id} started")
    await asyncio.sleep(2) 
    print(f"Task {task_id} finished")
    return f"results from task {task_id}"
async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )   
    print(results)

asyncio.run(main())


'''
Now, think deeper, Async is useful ONLY when waiting happens
eg: API calls, DB Queries, File reads

NOT useful for: CPU heavy tasks(math loops)
'''
# Pattern 1 - Timeout Handling

async def slow_task():
    await asyncio.sleep(5)
    return "Done"
async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
    except asyncio.TimeoutError:
        print("Task took too long")
asyncio.run(main())

# Pattern 2 - Semaphore(Limit Concurrency)
''' Imagine only 2 workers allowed at a time'''

sem = asyncio.Semaphore(2)

async def worker(task_id):
    async with sem:
        print(f"working on {task_id}")
        await asyncio.sleep(3)
async def main():
    try:
        result = await asyncio.gather(worker(1), worker(2), worker(3))
        return result
    except:
        print(f"No functions to gather")
asyncio.run(main())

# Pattern 3 - Async Queue [Producer - Consumer]
''' Real world: API requests pipeline
    Producer → adds tasks
    Consumer → processes tasks
'''
async def producer(queue):
    print("-------Producer---------")
    for i in range(1, 11):
        await asyncio.sleep(random.randint(1, 2)) #Simultate incoming tasks
        item = f"task-{i}"
        await queue.put(item)
        print(f"Produced {item}")
    
    #Signal consumers to stop
    await queue.put(None)
    
async def consumer(queue):
    print("--------consumer------")
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"Processing {item}")
        await asyncio.sleep(random.randint(1, 3)) # simulate work
        print(f" Done {item}")
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    
    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))
    
    await prod
    await queue.join() #wait untiull tasks processed
    
    cons.cancel() #stop consumer safely


# Exercise: 1 - API Timeout Simulator

async def fetch_api():
    delay = random.choice([1, 3])  # 1 sec (success) or 3 sec (timeout)
    await asyncio.sleep(delay)
    # await asyncio.sleep(random.randint(1, 5))
    print(f"sleep time range 1-5{delay}")
    return delay
async def main():
    try:
        result = await asyncio.wait_for(fetch_api(), timeout=2)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print(f"Task took longer than 2s ")
asyncio.run(main())


# Exercise 2- Limit concurrency

sem = asyncio.Semaphore(3)

async def lim_it(task_id):
    async with sem:
        print(f"working on {task_id}")
        # await asyncio.sleep(2)
        await asyncio.sleep(random.randint(1, 3))
        print(f"End {task_id}")
async def main():
    tasks = [lim_it(i) for i in range(1, 11)]
    await asyncio.gather(*tasks) # unpack/unzip list "*"

asyncio.run(main())

''' One main() per script -If you want both exercises together, do:

async def main():
    print("---- Exercise 1 ----")
    try:
        result = await asyncio.wait_for(fetch_api(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Timeout!")

    print("\n---- Exercise 2 ----")
    tasks = [lim_it(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)
'''

