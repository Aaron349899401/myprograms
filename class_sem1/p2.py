#Rollercoaster ride program
#input
#strings are alphanumeric characters and symbols trapped in quotation marks

place_in_line = int(input("what is your position:"))
num_cars = int(input("how cars are there in the train:"))
capacity = int(input("number of people a single car holds:"))

# processing
total_capacity = num_cars * capacity

if total_capacity >= place_in_line:
    print("YES!")
else:
    print("NO!")
