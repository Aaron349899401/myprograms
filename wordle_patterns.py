from collections import Counter
import math
 
# def ski(word_input, solutions_list):
#     result_list = []
#     num = 0
#     word = word_input.upper()
#     for solution in solutions_list:
#         result = ""
#         for i in range(len(solution)):
#             if solution[i] == word[i]:
#                 num += 1
#                 result += "G"
#             elif solution[i] in word:
#                 result += "Y"
#             elif solution[i] not in word:
#                 result += "B"
#         result_list.append(result)
#     return result_list

def ski(guess_word, solutions_list):
    result_list = []
    guess = guess_word.upper()
    
    for secret in solutions_list:
        secret = secret.upper()
        if len(guess) != len(secret):
            result_list.append("ERROR")
            continue
            
        result = [""] * len(guess)
        secret_counts = {}
        
        # Count letters in the secret word
        for char in secret:
            secret_counts[char] = secret_counts.get(char, 0) + 1
            
        # First pass: Greens
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                result[i] = "🟩"
                secret_counts[guess[i]] -= 1
        
        # Second pass: Yellows and Blacks
        for i in range(len(guess)):
            if result[i] == "":
                if guess[i] in secret and secret_counts[guess[i]] > 0:
                    result[i] = "🟨"
                    secret_counts[guess[i]] -= 1
                else:
                    result[i] = "⬛"
                    
        result_list.append("".join(result))
    return result_list

# Example usage
guess_word = input("Enter your guess word: ")
solutions_list = ["AGONY", "AXIAL", "CHIRP", "ACTOR", "ARDOR", "HOBBY", "STONE",
                  "TYING", "ATRIA", "CHALK", "RIDER", "CHORE", "PLEAD", "MIGHT",
                  "HEAVY", "GAUDY", "KNIFE", "LOFTY","BOOZE", "FENCE","SPORT",
                  "ETHER","PITCH", "EXCEL", "ISSUE"]

def analysis(guess_word, solutions_list):
    feedback_patterns = ski(guess_word, solutions_list)
    total = len(solutions_list)

    pattern_counts = Counter(feedback_patterns)

    distinct_patterns = len(pattern_counts)

    max_P = max(pattern_counts.values()) / len(solutions_list)

    largest_remaining = max(pattern_counts.values())

    probabilities = {x: y / total for x, y in pattern_counts.items()}

    entropy = -sum(
        p*math.log(p, 2) for p in probabilities.values()
    )

    expected_value = sum(
        (count / total) * count for count in pattern_counts.values()
    )
    return {
        "Guess": guess_word,
        "Distinct patterns": distinct_patterns,
        "Max Pi": max_P,
        "Largest remaining": largest_remaining,
        "Entropy": entropy,
        "Expected remaining": expected_value
    }
print(analysis(guess_word, solutions_list)) 
