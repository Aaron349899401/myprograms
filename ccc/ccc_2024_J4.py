def decode(keys, displayed):
    silly = ""
    quiet = ""
    store = {}
    if len(keys) != len(displayed):
        limit = min(len(keys), len(displayed))
        sus = ""
        visited = set()
        for b in range(limit):
                if keys[b] != displayed[b]:
                    if keys[b] not in visited:
                        visited.add(keys[b])
                        sus = keys[b]
                    else:
                        visited.remove(keys[b])
            quiet = "".join(list(visited))
    for i in range(len(keys)):
        store[keys[i]] = []
        if keys[i] != displayed[i]:
            store[keys[i]].append(displayed[i])

    for key, dis in store.items():
        new_displayed = ""
        if dis[0] == dis[1]:
            silly = dis[0]
            for x in displayed:
                if x == dis[0]:
                    x = key
                new_displayed += x
        if new_displayed == keys:
            quiet = "-"
            
    return silly, quiet

keys = "forloops"
displayed = "fxrlxxp"
print(decode(keys, displayed))
            
