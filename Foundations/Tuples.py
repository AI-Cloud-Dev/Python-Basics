# Task: The "Coordinate Record"

location = (40.7128, -74.0060)
try:
    location[0] = 50.00
except TypeError as e:
    print(f"\n Caught an Error: {e}")
    
(lat, lon) = location

print(f"Latitude: {lat}")
print(f"Longitude: {lon}")
