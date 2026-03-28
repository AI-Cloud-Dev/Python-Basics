import datetime

try:
    str = int("abc123")
except ValueError as e:
    print("OOps! error:", e)
finally: print("done")

# use append to avoid overwriting the error logs.

try:
    str = int("abc123")
except ValueError as e:
    with open("error_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        file.write(f"[{timestamp}] {e}\n")
    print("OOPS!! Error occurred :", e)
finally:
    print("Process complete")