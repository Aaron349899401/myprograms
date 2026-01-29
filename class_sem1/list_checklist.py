# Create an empty list
a_list = []
b_list = list()

# Determine if a string is empty
if not a_list:
    print("a_list is empty!")
if len(a_list) == 0:
    print("a_list is empty!")

# What does len(), sum(), min(), max() do when a list is an argument
c_list = [3,1,4,1,5,9]
print(len(c_list)) # output = 6
print(sum(c_list)) # output = 23
print(min(c_list)) # output = 1
print(max(c_list)) # output = 9

# Access individual items in a list
d_list = list("hello, world!")
print(d_list[0]) # output = "h"
print(d_list[-1]) # output = "!"
print(d_list[1:4]) # output = "e", "l", "l"

# Access the first, access the last item in a list
# Join two/multiple lists together
a = [3,1,4]
b = ["Marshall", "Freya", "Joy"]
c = a + b # creates new list of a and b joined
a.extend(b) # this mutates a to give the contents of b
for item in b: # adds one value at a time
    a.append(item)

# Reverse a list (two ways)
# Create a copy of a list (two ways)
# Compare lists for equality
# Determine if an item exists within a list
# Locate the index of an item within a list
# Count how often an item occurs within a list