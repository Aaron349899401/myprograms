import sys, re

N = int(sys.stdin.readline())

length_list = []
for _ in range(1, N+1):
    sentence = sys.stdin.readline()
    chars = re.findall(r"[a-zA-Z ]", sentence)
    length_list.append(len(chars))

length_list = map(str, length_list)
for item in length_list:
    sys.stdout.write(item + "\n")