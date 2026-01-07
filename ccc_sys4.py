import sys

count = 0
for _ in sys.stdin:
    count += 1

count = str(count)
sys.stdout.write(count)