def index_finder(integers, queries):
    indexes = []
    for index, query in enumerate(integers):
        if query in queries:
            indexes.append(index)
    return indexes

integers = [8, 3, 10, 6, 2]
queries = [10, 2, 8]
result = index_finder(integers, queries)
for i in result:
    print(i)