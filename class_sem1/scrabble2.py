def scrab(words):
    result = {}
    score_dic = {
        **dict.fromkeys("AEIOULNTRS", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10)
    }
    for word in words:
        result[word] = sum(score_dic.get(letter.upper(), 0) for letter in word)
    return result

words = ["poop", "pee", "amongus", "67"]
print(scrab(words))