#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import src.parser as pars


class Test_Interpreter:

    def test_get_question(self):
        """docstring"""
        assert self.pars.get_question() == str().lower()

    def test_remove_accents(self):
        """docstring"""
        quote = "où est la tour eiffel ?"
        assert self.pars.remove_accents(quote) == (
            "ou est la tour eiffel ?")

    def test_remove_punctuations(self):
        """docstring"""
        quote = "ou est la tour eiffel ?"
        assert self.pars.remove_punctuations(quote) == [
            'ou', 'est', 'la', 'tour', 'eiffel']

    def test_remove_current_word(self):
        """docstring"""
        words_quote = ['ou', 'est', 'la', 'tour', 'eiffel']
        assert self.pars.remove_current_word(words_quote) == (
            "tour eiffel")
