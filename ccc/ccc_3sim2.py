M = int(input("Enter your number of deliveries: "))

processing = []
for _ in range(M):
    hn, pd = map(int, input("Enter: ").split())
    processing.append((hn, pd))

dels = {}
for hn, pd in processing:
    dels[hn] = dels.get(hn, 0) + pd

max_pd = max(dels.values())
candidates = [hn for hn, pd in dels.items() if pd == max_pd]
print(min(candidates))
