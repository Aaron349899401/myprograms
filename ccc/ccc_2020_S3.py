from collections import Counter 
def permutations(needle, haystack):
    l = 0
    r = len(needle) - 1
    count = 0
    while r <= len(haystack):
        need = {}
        for char in needle:
            need[char] = need.get(char, 0) + 1
        
        hay = {}
        for char in haystack[l:r+1]:
            hay[char] = hay.get(char, 0) + 1
        
        fits = 0
        for char, num in need.items():
            if char not in hay.keys() or num != hay[char]:
                fits = 0
                break
            fits += 1
        
        count += fits // (r + 1)
        l += 1
        r += 1
    
    return count 

needle = input().strip()
haystack = input().strip()

print(permutations(needle, haystack))