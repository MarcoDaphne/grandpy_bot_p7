#!/usr/bin/env python3
# Coding: utf-8

import pytest

import grandpy.answer_manager as aswman

@pytest.mark.parametrize("test_input, expected", [
    ("", "Je n'ai pas compris"),
    (" ", "Je n'ai pas compris"),
    ("Aahhh!", "Je n'ai pas compris"),
    ("Où se trouve la Tour Eiffel ?", "Biensur mon enfant")
])
def test_check_parser(monkeypatch, test_input, expected):
    def fake_check_parser(self, query):
        if query == "" or query == " " or len(query) <= 6:
            return "Je n'ai pas compris"
        else:
            return "Biensur mon enfant"

    monkeypatch.setattr(
        "grandpy.answer_manager.AnswerManager.check_parser",
        fake_check_parser
        )
    manager = aswman.AnswerManager()
    assert manager.check_parser(test_input) == expected


@pytest.mark.parametrize("address, location, expected", [
    (None, [None, None], "Pas d'informations sur cet endroit"),
    ("5 rue...PARIS", [1.8556, 2.22563], "C'est ici...")
])
def test_check_locater(monkeypatch, address, location, expected):
    def fake_check_locater(self, address, location):
        if address == None and location == [None, None]:
            return "Pas d'informations sur cet endroit"
        else:
            return "C'est ici..."

    monkeypatch.setattr(
        "grandpy.answer_manager.AnswerManager.check_locater",
        fake_check_locater
        )
    manager = aswman.AnswerManager()
    assert manager.check_locater(address, location) == expected


@pytest.mark.parametrize("test_input, expected", [
    ([None, None], "Pas plus d'informations sur ce lieu"),
    (["wikipedia summary", "wikipedia url"], "D'ailleurs, sais tu que...")
])
def test_check_storyteller(monkeypatch, test_input, expected):
    def fake_check_storyteller(self, location):
        if location == [None, None]:
            return "Pas plus d'informations sur ce lieu"
        else:
            return "D'ailleurs, sais tu que..."

    monkeypatch.setattr(
        "grandpy.answer_manager.AnswerManager.check_storyteller",
        fake_check_storyteller
        )
    manager = aswman.AnswerManager()
    assert manager.check_storyteller(test_input) == expected
