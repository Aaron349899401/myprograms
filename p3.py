# Donut 
donut_count = int(input("Enter the number of donuts:"))
events = int(input("Enter the number of events:"))

# we stop when no donut or no event
#while is a repetitive if statement (loop)
#two different if's = not linked
current_event = 1 # Personally I do 0
while current_event <= events and donut_count >= 0: 
    event_type = input("+ or -?: ")
    donut_amount = int(input("Enter donut amount: "))
    if event_type == "+":
        donut_count += donut_amount
    elif event_type == "-":
        donut_count-= donut_amount
    else:
        print("not an option!")
# end of while loop
print(f"You have {donut_count} donuts left")