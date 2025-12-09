import random

with open("solutions.txt", "r") as f:
    solutions = [word.strip().upper() for word in f.readlines()]

sampled_words = random.sample(solutions, 25)

for i, word in enumerate(sampled_words, 1):
    print(f"{i}. {word}")
