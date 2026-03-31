# Args = A list of extra values
# Kwargs = A dictionary of extra named settings (like color = "red", size = 10)
# *args and **kwargs = Allow a function to take any number of arguments

def log_event(event:str, *tags: str, **metadata):
    print(f"[{event}] tags = {tags} meta = {metadata}")
    
log_event("login", "auth", "security", user_id = 53, ip ="10.0.0.0.9")

def demo(a, *args, **kwargs):
    print(a, args, kwargs)

demo(1, 2, 3, 4, 5, 6, 7) # kwargs = {}

# Mix of positional + keyword
demo(1, 2, 3, x=10, y=20)

# No extra positional, only keywords
demo(1, x=90, y=98) # args = () empty tuple

demo("sree", 2, 3, x=7, y=6)
demo(a=5, x=1, y=2) # args = () empty tuple

nums = [10, 20, 30]
info = {"user": "alice", "role": "IT"}
demo(1, *nums, **info)

# Log style

def log_events(event, *tags, **meta):
    print(event, tags, meta)

log_events("upload", "file", "image", size = 2048, format = "png")


