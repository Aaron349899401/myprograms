# AMOGUS
def is_palindrome(word):
    return word == word[::-1]

word = input("Enter your word: ")
if is_palindrome:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome!")