# ── collections module (MUST KNOW) ───────────────────────
from collections import defaultdict, Counter, deque
import string

freq   = Counter(["a","b","a","c","a"])  # Counter({'a':3,'b':1,'c':1})
graph  = defaultdict(list)                # default value = empty list
queue  = deque([1,2,3])                  # O(1) append/pop from both ends
queue.appendleft(0)

print(freq)
print(graph)
print(queue)

c = Counter(["a", "b", "a"])
print(c)

# Default dict
d= defaultdict(list)
d["a"].append(1)

# dequeue
q = deque()
q.append(1)
print(q.popleft())

# Exercise 1: count word frequency in sentence

sent= "this pick is that puck pick with pick n puck luck with pick"

clean_sent = sent.lower().translate(str.maketrans("", "", string.punctuation))

words = clean_sent.split()

word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")
    
# Exercise 2: Group numbers

number = [1, 2, 3, 4, 5]

even = [x for x in number if x%2==0]
odd = [x for x in number if x%2!=0]

even_count = Counter(even)
odd_count = Counter(odd)

result = {
    "even": even_count,
    "odd": odd_count
}
print(result)
result = {
    "even": even,
    "odd": odd
}
print(result)

# Exercise 3 - Build queue system using deque

# Initializing Empty Queue
queue = deque()

# ---- Producer: Add items to the queue
queue.append("task1")
queue.append("task2")
queue.append("task3")
print("Queue after adding tasks:", queue)

# ---- Consumer: Process items from the queue
while queue:
    task = queue.popleft() #FIFO: get the first task First in First Out
    
    print(f"Processing {task}")
print("Queue empty:", queue)
