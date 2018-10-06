#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import re

from .constants import accents
from .constants import common_words


class Parser:
    def __init__(self):
        self.question = None

    def set_question(self, question):
        """docstring"""
        self.question = question.lower().strip()

    def remove_accents(self):
        """docstring"""
        for (character, accented_characters) in accents.items():
            for accented_character in accented_characters:
                self.question = self.question.replace(
                    accented_character, character)
        return self.question

    def remove_punctuations(self):
        """docstring"""
        self.question = re.sub(r"\W+", " ", self.question).strip()
        return self.question

    def remove_current_word(self):
        search_word = []
        self.question = self.question.split()
        for word in self.question:
            if word not in common_words:
                search_word.append(word)
        self.question = " ".join(search_word)
        return self.question


if __name__ == '__main__':
    question_interpreted = Parser()
    question_interpreted.set_question("""Où est le truffaut le plus proche ?""")
    question_interpreted.remove_accents()
    question_interpreted.remove_punctuations()
    question_interpreted.remove_current_word()
