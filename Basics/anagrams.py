# 2. Check for Anagrams
# Write a Python function to check if two given strings are anagrams of each other.
# Input: "listen", "silent"
# Output: True

s1 = "listen"
s2 = "silent"
if sorted(s1)==sorted(s2):
    print(True)
else:
    print(False)