def match(lih, queries):
    result_list = []
    for integer in queries:
        if integer in lih:
            result_list.append("YES")
        else:
            result_list.append("NO")
    return result_list

integer = int(input("Enter the number of integers in your list: "))
lih = set(map(int, input("Enter your list of integers: ").split()))
Q = int(input("Enter your number of queries: "))
queries = []
for _ in range(Q):
    queries.append(int(input("Enter your querie: ")))

booleans = match(lih, queries)
for i in booleans:
    print(i)