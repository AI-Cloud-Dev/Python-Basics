# Immutable = cannot change (String, int, tuple)
#  Mutable = can change (List, dict, set)

x = 10
x = 20 # new object
print(x)

# Mutable
lst = [1, 2]
lst.append(3) # same object modified
print(lst)

# Mutable
x = 10
print(id(x))
x = 20
print(id(x))

# Mutable
def lst_mem(my_lst):
    my_lst.append(3)
    print(my_lst)
    
lst_mem([1, 2, 3])

# Mutable trap
def add_item(item, my_list=[]):
    my_list.append(item)
    print(my_list)
    return my_list
add_item(4)
add_item(5)

# Mutable
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
        print(my_list)
add_item(4, [1, 2, 3])
