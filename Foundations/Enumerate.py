# Enumerate = to include Index

names = ["a", "b", "c"]
for i, name in enumerate(names):
    print(i, name)
    
for i, name in enumerate(names, start=1):
    print(i, name)
    
