#Write a Python function to find the first non-repeating character in a given string and return its index.
#Input: "swiss"
#Output: 1 (for 'w' in "swiss")

def first_non_repeating_char(s):
    char_count = {}

    #char count
    for char in s:
        char_count[char] = char_count.get(char, 0)+1

    #find first unique character
    for i, char in enumerate(s):
        if char_count[char]==1:
            return i
    return -1

print(first_non_repeating_char('swiss'))