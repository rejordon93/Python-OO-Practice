"""Word Finder: finds random words from a dictionary."""


import random


class WordFinder:

    def __init__(self, word_path):
        with open(word_path) as dict_file:
            self.words = self.parse(dict_file.readlines())
        print(f"{len(self.words)} words read")

    def parse(self, lines):
        return [w.strip() for w in lines]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):

    def parse(self, lines):
        """Parse lines -> list of words, skipping blanks/comments."""

        return [w.strip() for w in lines if w.strip() and not w.startswith("#")]

    
