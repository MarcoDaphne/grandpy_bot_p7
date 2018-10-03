#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import re

import .constants as c


class Parser:
    def __init__(self):
        self.question = None

    def set_question(self, question):
        """docstring"""
        self.question = question.lower().strip()

    def remove_accents(self):
        """docstring"""
        for (character, accented_characters) in c.accents.items():
            for accented_character in accented_characters:
                self.question = self.question.replace(
                    accented_character, character)
        return self.question

    def remove_punctuations(self):
        """docstring"""
        self.question = re.sub(r"\W+", " ", self.question).strip()
        self.question = self.question.split()
        return self.question

    def remove_current_word(self):
        print(self.question)


if __name__ == '__main__':
    question_interpreted = Parser()
    question_interpreted.set_question('Où se trouve la Tour Eiffel ?')
    question_interpreted.remove_accents()
    question_interpreted.remove_punctuations()
    question_interpreted.remove_current_word()
