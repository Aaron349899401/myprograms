import sys

N = int(sys.stdin.readline())
lih = []
for _ in range(1, N+1):
    lih.append(sys.stdin.readline())

max_value = max(lih)
sys.stdout.write(max_value)

# how to run code:

# echo "3`n2`n3`n4`n" | python ccc_sys2.py

# @"
# 5
# 10
# 3
# 22
# 7
# 15
# "@ | python script.py