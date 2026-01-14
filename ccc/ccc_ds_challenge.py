def match(target, string):
    seen = set()
    for x in string:
        if target - x in seen:
            return True
        seen.add(x)
    return False
target = 10
string = [1, 4, 5, 6, 8]
res = match(target, string)
if res:
    print("YES")
else:
    print("NO")