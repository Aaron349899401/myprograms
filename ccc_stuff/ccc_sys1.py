import sys

num_list = []
for data in sys.stdin.readline():
    if data.isdigit():
        num_list.append(int(data))
print(sum(num_list))
