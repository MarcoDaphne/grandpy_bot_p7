#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import grandpy.locater as loc
import grandpy.parser as pars


def test_search_place(monkeypatch):
    def fake_get(url, params):
        class FakeResponse:
            fake_json = {
                'candidates': [
                    {'place_id': 'ChIJLU7jZClu5kcR4PcOOO6p3I0'}
                    ], 
                'debug_log': {'line': []}, 
                'status': 'OK'
                }
            def json(self):
                return FakeResponse.fake_json
        return FakeResponse()
    monkeypatch.setattr("grandpy.locater.requests.get", fake_get)
    keyword = pars.Parser()
    keyword.set_question('tour eiffel')
    locater = loc.Locater(keyword)
    assert locater.search_place() == 'ChIJLU7jZClu5kcR4PcOOO6p3I0'


def test_get_place_details(monkeypatch):
    def fake_get(url, params):
        class FakeResponse:
            fake_json = {
                'html_attributions': [],
                'result': {
                    'formatted_address': "Square de l'Atomium, 1020 Bruxelles, Belgique",
                    'geometry': {
                        'location': {
                            'lat': 50.894941,
                            'lng': 4.341547
                            },
                        'viewport': {
                            'northeast': {
                                'lat': 50.8962620302915,
                                'lng': 4.343035
                                },
                            'southwest': {
                                'lat': 50.8935640697085,
                                'lng': 4.3401166
                                }
                            }
                        }
                    },
                    'status': 'OK'
                }
            def json(self):
                return FakeResponse.fake_json
        return FakeResponse()
    
    def fake_search():
        return 'ChIJAQAAAKzDw0cRCTemaB0Hk1I'
    
    monkeypatch.setattr("grandpy.locater.requests.get", fake_get)
    keyword = pars.Parser()
    keyword.set_question('atomium')
    locater = loc.Locater(keyword)
    monkeypatch.setattr("grandpy.locater", "search_place", fake_search)
    assert locater.set_place_details() == {
        'formatted_address': "Square de l'Atomium, 1020 Bruxelles, Belgique",
        'geometry': {
            'location': {
                'lat': 50.894941,
                'lng': 4.341547
                },
            'viewport': {
                'northeast': {
                    'lat': 50.8962620302915,
                    'lng': 4.343035
                    },
                'southwest': {
                    'lat': 50.8935640697085,
                    'lng': 4.3401166
                    }
                }
            }
        }
