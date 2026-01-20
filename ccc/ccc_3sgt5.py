def ranking(bros):
    bros = sorted(bros, key=lambda x: (-x[1], x[0]))
    return [name for name, score in bros]

N = int(input("Enter your number of people: "))
bros = []
for _ in range(N):
    n, s = input("Enter your person and score: ").split()
    bros.append((n, int(s)))

result = ranking(bros)
for i in result:
    print(i)