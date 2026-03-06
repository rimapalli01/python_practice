#Write a Python function to perform basic string compression using the counts of repeated characters.
#Input: "aabcccccaaa"
#Output: "a2b1c5a3"

def compress_string(s):
    result =""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count =1

    result += s[-1] + str(count)
    return result

print(compress_string("aabcccccaaa"))