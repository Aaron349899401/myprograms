def frequent(strings):  
    result = []  
    for string in strings:
        freq = {}
        for char in string:
            freq[char] = freq.get(char, 0) + 1

        max_freq = max(freq.values())
        most_common = [char for char, count in freq.items() if count == max_freq]

        result.append(max(most_common))
    return result
strings = ["banana", "apple", "missisipi"]
print(frequent(strings))