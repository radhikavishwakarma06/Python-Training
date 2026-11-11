# Reverse a sentence.
s = "python is a programming langauge"
words = s.split()
res = ""

for char in words[::-1]:
    res = res + char + " "

print("Reversed sentence: ", res)


# • Check whether a word is a palindrome.

def is_palindrome(s):
    s = s.replace(" ","").lower()
    return s==s[::-1]


is_palindrome("Madam")


# • Count vowels and consonants.
s = "programming"

vowels = 0
consonants = 0

for char in s.lower():
        if char in "aeiou":
                vowels += 1
        else:
               consonants  += 1


print("Total vowels", vowels)
print("Total consonants", consonants)


# • Count total words.

s = "python is a programming language"
words = s.split()

print("total words: ", len(words))


# • Remove extra spaces.

sentence = " python is a   programming   language"

result = " ".join(sentence.split())

print("After removing extra spaces:", result)


# • Count character frequency.

text = "banana"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)


# #Find the first non-repeating character.
text = "spaces"

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

result = None
for ch in text:
    if freq[ch] == 1:
        result = ch
        break

print(result)