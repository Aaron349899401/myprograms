from math import gcd
def is_sweets(cards):
    cards.sort(reverse=True)
    for c in cards:
        