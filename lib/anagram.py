# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Initialize the Anagram instance with the given word.
        self.word = word

    def match(self, possible_anagrams):
        # Sort the letters of the given word for comparison
        sorted_word = sorted(self.word)

        # Use list comprehension to find all matching anagrams
        return [anagram for anagram in possible_anagrams if sorted(anagram) == sorted_word]
