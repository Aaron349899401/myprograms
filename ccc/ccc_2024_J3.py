def fix(scores):
    return sorted(scores, reverse=True)

result = fix(scores)
freq = {}
 count = result.count(result[2])
print(f"{result[2]}: {count}")