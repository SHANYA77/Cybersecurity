sentence = input("Enter sentence: ")

words = sentence.split()
vowels = "aeiouAEIOU"

word_count = len(words)
vowel_count = 0
consonant_count = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Word frequency
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Words:", word_count)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Frequency:", freq)
