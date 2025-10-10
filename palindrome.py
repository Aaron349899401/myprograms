def is_anagram(text1, text2):
    wow = text1.lower().replace(" ", "")
    noway = text2.lower().replace(" ", "")
    return wow == noway[::-1]
text1 = input("Enter your first word: ")
text2 = input("Enter your second word: ")
if is_anagram(text1, text2):
    print("Anagram!")
else:
    print("nah!")

