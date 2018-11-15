#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import grandpy.answer as answ


googlemaps_list_empty = []
googlemaps_list = [
    {
        'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
        'geometry': {
            'location': {
                'lat': 48.85837009999999,
                'lng': 2.2944813
            }
        }
    }
]

wikipedia_list_empty = []
wikipedia_list = [
    'Le Jules Verne',
    'Exposition universelle de Paris de 1889',
    'Buste de Gustave Eiffel par Antoine Bourdelle',
    'Tour Eiffel',
    'Rives de la Seine à Paris',
    'Avenue Gustave-Eiffel',
    'Allée Jean-Paulhan',
    "Grande lunette de l'exposition universelle de Paris 1900",
    'Allée des Refuzniks',
    'Allée Paul-Deschanel'
]


def test_answer_user_query(monkeypatch):
    class FakePage:
        summary = "Résumé sur Allée Jean-Paulhan"
        url = "url Wikipédia Allée Jean-Paulhan"

    def fake_geocode(self, question):
        return googlemaps_list

    def fake_geosearch(self, latitude, longitude):
        return wikipedia_list

    def fake_page(self, title):
        return FakePage()

    def fake_random_choice_title(self):
        return 'Allée Jean-Paulhan'

    def fake_grandpy_say(self):
        return 'Ce que Grandpy dit à ce moment'

    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )

    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )

    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.page",
        fake_page
    )

    monkeypatch.setattr(
        "grandpy.storyteller.random.choice",
        fake_random_choice_title
    )

    monkeypatch.setattr(
        "grandpy.answer_manager.random.choice",
        fake_grandpy_say
    )

    answer = answ.Answer()
    query = "Salut GrandPy, où se trouve la Tour Eiffel ?"
    assert answer.answer_user_query(query) == {
        'Parser': 'Ce que Grandpy dit à ce moment',
        'Locater': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                'location': [
                    48.85837009999999,
                    2.2944813
                ]
            }
        },
        'StoryTeller': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'summary': 'Résumé sur Allée Jean-Paulhan',
                'url': 'url Wikipédia Allée Jean-Paulhan'
            }
        }
    }


def test_answer_user_query_partialy(monkeypatch):
    def fake_geocode(self, question):
        return googlemaps_list

    def fake_geosearch(self, latitude, longitude):
        return wikipedia_list_empty

    def fake_grandpy_say(self):
        return 'Ce que Grandpy dit à ce moment'

    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )

    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )

    monkeypatch.setattr(
        "grandpy.answer_manager.random.choice",
        fake_grandpy_say
    )

    answer = answ.Answer()
    query = "Salut GrandPy, où se trouve la Tour Eiffel ?"
    assert answer.answer_user_query(query) == {
        'Parser': 'Ce que Grandpy dit à ce moment',
        'Locater': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                'location': [
                    48.85837009999999,
                    2.2944813
                ]
            }
        },
        'StoryTeller': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'summary': None,
                'url': None
            }
        }
    }


def test_answer_user_query_failed(monkeypatch):
    def fake_geocode(self, question):
        return googlemaps_list_empty

    def fake_grandpy_say(self):
        return 'Ce que Grandpy dit à ce moment'

    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )

    monkeypatch.setattr(
        "grandpy.answer_manager.random.choice",
        fake_grandpy_say
    )

    answer = answ.Answer()
    query = "Où se trouve le Mac donalds de je ne sais où ?"
    assert answer.answer_user_query(query) == {
        'Parser': 'Ce que Grandpy dit à ce moment',
        'Locater': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'address': None,
                'location': [
                    None,
                    None
                ]
            }
        },
        'StoryTeller': {
            'say': 'Ce que Grandpy dit à ce moment',
            'data': {
                'summary': None,
                'url': None
            }
        }
    }
