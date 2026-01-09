def cleaner(text):
    stack = []
    for char in text:
        if stack and stack[-1] == char:
            stack.pop()   # remove the previous matching char
        else:
            stack.append(char)
    return "".join(stack)

text = "abbaca"
print(cleaner(text))   # Output: "ca"



