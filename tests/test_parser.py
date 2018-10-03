#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import grandpy.parser as pars


class TestParser:

    def test_remove_accents(self):
        """docstring"""
        question = "Où est la Tour Eiffel ?"
        parser = pars.Parser()
        parser.set_question(question)
        assert parser.remove_accents() == (
            "ou est la tour eiffel ?")

    #def test_remove_punctuations(self):
        #"""docstring"""
        #quote = "ou est la tour eiffel ?"
        #assert self.pars.remove_punctuations(quote) == [
            #'ou', 'est', 'la', 'tour', 'eiffel']

    #def test_remove_current_word(self):
        #"""docstring"""
        #words_quote = ['ou', 'est', 'la', 'tour', 'eiffel']
        #assert self.pars.remove_current_word(words_quote) == (
            #"tour eiffel")
