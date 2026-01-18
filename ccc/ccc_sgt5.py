def poop(people):
    return sorted(people, key=lambda x: (-x[1], x[0]))
# the order in the sorting lambda key: tuples are sorted in order
# if the first item is equal, it checks the second and so on

N = int(input("Enter your number of contestants: "))
people = []
for _ in range(N):
    p, s = input("Enter your person and score: ").split()
    people.append((p, int(s)))

result = poop(people)
for name, score in result: # basically saying for tuple in list, the two comma seperated items is the tuple
    print(name)

