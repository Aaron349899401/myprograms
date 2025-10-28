# Painting Fences
def wow(poop):
    even_list = [num for num in poop if num % 2 == 0]
    odd_list = [num for num in poop if num % 2 != 0]
    sumting = max(even_list, odd_list, key=len)
    return [] if len(even_list) == len(odd_list) else sumting

pee = input("Enter your values: ")
poop = [int(x.strip()) for x in pee.split(",")]
print(wow(poop))