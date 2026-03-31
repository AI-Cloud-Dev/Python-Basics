# Zip  =  Zipping them together

names = ["a", "b"]
ages = [20, 30]

for n, a in zip(names, ages):
    print(n, a)
    
zip_data = zip(names, ages)

print(zip_data)

# converting the zip data into list
print(list(zip_data))
    

# "Unzip" (The Asterisk *)
data = [("sree", "dev"), ("kat", "IT"), ("Pat", "Test")]

# Unzipping
names_back, roles_back = zip(*data)

print(names_back)
print(roles_back)

# Dict
lst1= ["a", "b"]
lst2 = [1, 2]

print(dict(zip(lst1, lst2)))

# ── zip and map ───────────────────────────────────────────
keys   = ["name", "age"]
values = ["Arjun", 28]
profile = dict(zip(keys, values))   # {'name': 'Arjun', 'age': 28}
doubled = list(map(lambda x: x*2, [1,2,3]))  # [2, 4, 6]