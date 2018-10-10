#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import requests

import grandpy.parser as pars
from .constants import url_search
from .constants import url_details
from .constants import fields
from .constants import key


class Locater:
    """docstring"""

    def __init__(self, keyword):
        self.keyword = keyword
        self.address = str()
        self.location = str()

    def search_place(self):
        """docstring"""
        parameters = {
            'input': self.keyword.question,
            'inputtype': 'textquery',
            'fields': "place_id",
            'key': key
        }
        response = requests.get(url_search, params=parameters)
        print(response.json()['candidates'][0].get('place_id'))
        return response.json()

    def get_place_details(self):
        """docstring"""
        id = self.search_place()['candidates'][0].get('place_id')
        parameters = {
            'key': key,
            'place_id': id,
            'language': 'fr',
            'fields': fields
        }
        response = requests.get(url_details, params=parameters)
        print(response.json()['result'].get('formatted_address'))
        print(response.json()['result'].get('geometry').get('location'))
        return response.json()


if __name__ == "__main__":
    question_parse = pars.Parser()
    question_parse.set_question("Où puis-je trouver un mèdecin à LONGJUMEAU ?")
    question_parse.remove_accents()
    question_parse.remove_punctuations()
    question_parse.remove_current_word()
    place_locate = Locater(question_parse)
    place_locate.get_place_details()
