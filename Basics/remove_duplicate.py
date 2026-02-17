# 3. Remove Duplicate Characters
# Write a Python function to remove all duplicate characters in a given string while preserving the order of the remaining characters.
# Input: "programming"
# Output: "progamin"
s = "programming"
chars= set()
output = ""

for ch in s:
    if ch not in chars:
        output += ch
        chars.add(ch)

print(output)
