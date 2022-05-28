
def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    return False

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

print(find_anagram(word1, word2))
