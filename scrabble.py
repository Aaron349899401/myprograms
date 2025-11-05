# 3a)
def scrab_score(bum):
    score = {
        **dict.fromkeys("AEIOULNSTR", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10)
    } 

    return sum(score.get(item.upper(), 0) for item in bum)
bum = "wowzers"
word_list = ["poopoo", "peepee", "ghana"]
result3a = scrab_score(bum)
print(f"The total scrabble score of your word is: {result3a}")

# 3b)
def ww(word_list):
    collection = []
    word_score = 0
    for item in word_list:
        word_score += scrab_score(letter)
        collection.append(word_score)
    return collection

word_list = ["poopoo", "pee", "ghana", "china"]
result3b = ww(word_list)
print(f"The scrabble scores of your word list is: {result3b}")

# 3c
def www(word_list):
    swapped = True
    while swapped:
        swapped = False
        for index in range(1, len(word_list)):
            if scrab_score(word_list[index - 1]) < scrab_score(word_list[index]):
                word_list[index - 1], word_list[index] = word_list[index], word_list[index - 1]
                swapped = True
    return word_list

result3c = www(word_list)
print(f"Here is your sorted word list: {result3c}")
