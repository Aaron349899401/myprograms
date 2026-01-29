import re
def queries_fixer(queries):
    queries_fixed = []
    for item in queries:
        placeholder = set(re.findall(r"\d+", item))
        queries_fixed.append(placeholder)
    return queries_fixed

def get_prefix_sums(arr, queries, q):
    l = [x[1] for x in queries]
    r = [y[4] for y in queries]
    while q > 0:
        results = []
        n = len(arr)
        prefix_sums = [0] * (n+1)
        for i in range(l, r+1):
            prefix_sums[i] = prefix_sums[i-1] + arr[i-1]
        results.append(prefix_sums[r+1])
        q -= 1
    return results

n = int(input("Enter the number of days: "))
wow = input("Enter: ")
arr = [10, 20, 30, 40, 50]
q = int(input("Enter the number of queries: "))
go = input("Enter list: ")
queries = [y.split() for y in go.strip(",")]

for j in get_prefix_sums(arr, queries, q):
    print(j)