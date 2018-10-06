#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import pytest

import grandpy.parser as pars


class TestParser:


    @pytest.mark.parametrize("test_input, expected", [
        ("Où est la Tour Eiffel ?", "ou est la tour eiffel ?"),
        ("àâäã éèêë îï ôö ûüù", "aaaa eeee ii oo uuu"),
        ("", "")
    ])
    def test_remove_accents(self, test_input, expected):
        parser = pars.Parser()
        parser.set_question(test_input)
        assert parser.remove_accents() == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("ou est la tour eiffel ?", "ou est la tour eiffel"),
        (".,;:?!()[]/", ""),
        ("", "")
    ])
    def test_remove_punctuations(self, test_input, expected):
        parser = pars.Parser()
        parser.set_question(test_input)
        assert parser.remove_punctuations() == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("ou est la tour eiffel", "tour eiffel"),
        ("ou est le macdonalds le plus proche", "macdonalds"),
        ("raconte moi l histoire de l arc de triomphe", "arc triomphe"),
        ("", "")
    ])
    def test_remove_current_word(self, test_input, expected):
        parser = pars.Parser()
        parser.set_question(test_input)
        assert parser.remove_current_word() == expected
