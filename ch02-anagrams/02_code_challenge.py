# Python code​​​​​​‌‌‌​​​​​​​‌​‌‌​​‌‌​‌​​​‌‌ below
# Use print("messages...") to debug your solution.

import itertools

show_expected_result = False
show_hints = False

palindrome = []
def palindromes(anagrams_by_signature):
    # Your code goes here.
    for words in anagrams_by_signature.values():
        for word1, word2 in itertools.combinations(words, 2):
            if word1 == word2[::-1] and len(word1) >= 7:
                palindrome.append({word1, word2})
    return palindrome