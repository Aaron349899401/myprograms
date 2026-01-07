import sys, re

N = int(sys.stdin.readline())
product_list = []
for _ in range(1, N+1):
    bruh = sys.stdin.readline()
    bruh = re.sub(r"\D", "", bruh)
    product = int(bruh[0]) * int(bruh[1])
    product_list.append(product)

product_list = map(int, product_list)
result = str(sum(product_list))
sys.stdout.write(result)

# the @""@ input method is better!