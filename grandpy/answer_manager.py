#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import random

from .constants import say

class AnswerManager:
    """docstring"""


    def select_answer(self, answer):
        """docstring"""
        return random.choice(answer)


    def check_parser(self, query):
        """docstring"""
        if query == "" or query == " " or len(query) <= 6:
            return self.select_answer(say['not_understand'])
        else:
            return self.select_answer(say['understand'])


    def check_locater(self, address, location):
        """docstring"""
        if address == None and location == [None, None]:
            return self.select_answer(say['not_find'])
        else:
            return self.select_answer(say['find'])


    def check_storyteller(self, location):
        """docstring"""
        if location == [None, None]:
            return self.select_answer(say['not_tell'])
        else:
            return self.select_answer(say['tell'])


if __name__ == "__main__":
    grandpy = AnswerManager()