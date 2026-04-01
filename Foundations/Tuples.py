# Task: The "Coordinate Record"

location = (40.7128, -74.0060)
try:
    location[0] = 50.00
except TypeError as e:
    print(f"\n Caught an Error: {e}")
    
(lat, lon) = location

print(f"Latitude: {lat}")
print(f"Longitude: {lon}")

# ── Tuples — immutable, hashable (can be dict key) ────────
point = (10.5, 20.3)
x, y = point   # tuple unpacking
coords = {(0,0): "origin", (1,0): "right"}
