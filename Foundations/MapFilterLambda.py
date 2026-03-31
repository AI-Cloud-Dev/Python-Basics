# Map = Applies a function to every item in a list
# Filter = Keeps only items which meets 
# Lambda = an anonymous, one line function sq= lambda x: x*x

nums = [1, 2, 3]
map_test = list(map(lambda x: x*2, nums))
filter_test = list(filter(lambda x: x%2==0, nums))
print(map_test)
print(filter_test)


map1 = list(map(lambda x: x+x, nums))
filter1 =list(filter(lambda x: x%2!=0, nums))

print(map1)
print(filter1)