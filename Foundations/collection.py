# ── collections module (MUST KNOW) ───────────────────────
from collections import defaultdict, Counter, deque

freq   = Counter(["a","b","a","c","a"])  # Counter({'a':3,'b':1,'c':1})
graph  = defaultdict(list)                # default value = empty list
queue  = deque([1,2,3])                  # O(1) append/pop from both ends
queue.appendleft(0)

print(freq)
print(graph)
print(queue)
