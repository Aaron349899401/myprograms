# String Checklist
# Create an empty string
empty_string = ""
ver2 = ''
# Determine if a string is empty
if not str_var:
    print("str_var is empty!")
if len(str_var) == 0:
    print("str_var is empty!")
# Format a string to contain dynamic data
name = "knitter"
str_var = f"Hello {name}!"
# Access individual characters/items in a string
print(name[0]) # --> k
print(name[-2]) # --> e
# Access the first, access the last item in a string
print(name[0]) # zero is always the first
print(name[len(name)-1]) # this gives last
print(name[-1]) # same
# Join two/mutiple strings together
a = "poo"
b = "poo"
c = a + b #concatenation
print(c) # --> poopoo
# Reverse a string
chigga = poopy
wow = chigga[::-1]
ver2 = "".join(reversed(chigga))
print(wow + ver2)
# Create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp
# Compare strings for equality
noway = "sigma"
bruh = "haw"
status = noway == bruh
# Determine the minimum and maximum value within a string
yo = "skibidi"
print(max(yo)) # Grabs the latest most within ACSII table
print(min("1", "2", "3", "!"))
# Determine if an item or a pattern exists within a string
word = "poopoo platter"
if "poo" in word.strip():
    print("THERE IS POO!")
# Locate the index of an item or a pattern within  a string
poop_location = word.find("poo")
poop_location = word.index("poop")
# Count how often an item or a pattern occurs within a string
poop_count = word.count("poo")
# Convert all items in a string to uppercase/lowercase
yell_hydroflask = "hyrdoflask".upper()
chill_hydroflask = yell_hydroflask.lower()
# Determine if the string can be convrted to an integer
if str_num.isdigit() == True:
    print("YEAH!")
# Convert a string to an integer
str_num = "67"
if str_num.isdigit():
    num = int(str_num)
# Determine is a string only contains alphabetical characters
word = "rizz".isalpha()
# Remove non-alphabetical charaters from a string
gibberish = "skibidi!@@#@!%#$@$rizzler"
clean = ""
i = 0
while i < len(gibberish):
    if gibbersih[i].isalpha():
        clean += gibberish[i]
    i += 1
# Remove all alphabetical characters from a string
gibberish = "skibidi!@@#@!%#$@$rizzler"
clean = ""
i = 0
while i < len(gibberish):
    if not gibbersih[i].isalpha():
        clean += gibberish[i]
    i += 1
# Remove all whitespaces from a string
noneya = "b u si ness"
noneya = noneya.replace(" ", "")
# Sort a string in ASCII order or reverse-ASCII order
# Determine if a string follows a ruleset. (e.g. proper email)