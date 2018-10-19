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
        self.address = None
        self.latitude = None
        self.longitude = None

    def search_place(self):
        """docstring"""
        parameters = {
            'input': self.keyword.question,
            'inputtype': 'textquery',
            'fields': "place_id",
            'key': key
        }
        response = requests.get(url_search, params=parameters)
        return response.json()['candidates'][0].get('place_id')

    def get_place_details(self):
        """docstring"""
        place_id = self.search_place()
        parameters = {
            'key': key,
            'place_id': place_id,
            'language': 'fr',
            'fields': fields
        }
        response = requests.get(url_details, params=parameters)
        return response.json()['result']

    def get_address(self):
        self.address = self.get_place_details().get('formatted_address')
        return self.address

    def get_latitude(self):
        location = self.get_place_details()['geometry'].get('location')
        self.latitude = location.get('lat')
        return self.latitude

    def get_longitude(self):
        location = self.get_place_details()['geometry'].get('location')
        self.longitude = location.get('lng')
        return self.longitude

    def show_result(self):
        print("adresse: {}".format(self.address))
        print("latitude: {}".format(self.latitude))
        print("longitude: {}".format(self.longitude))
        print(self.search_place())


if __name__ == "__main__":
    question_parse = pars.Parser()
    question_parse.set_question("Bonjour GrandPY, où se trouve la Montagne pelée ?")
    question_parse.remove_accents()
    question_parse.remove_punctuations()
    question_parse.remove_current_word()
    place_locate = Locater(question_parse)
    place_locate.get_address()
    place_locate.get_latitude()
    place_locate.get_longitude()
    place_locate.show_result()
