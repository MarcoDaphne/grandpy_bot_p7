#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import pytest

import grandpy.locater as loc


data_list_1 = [
    {
        'address_components': [
            {
                'long_name': 'Champ de Mars',
                'short_name': 'Champ de Mars',
                'types': ['establishment', 'point_of_interest']
            },
            {
                'long_name': '5',
                'short_name': '5',
                'types': ['street_number']
            },
            {
                'long_name': 'Avenue Anatole France',
                'short_name': 'Avenue Anatole France',
                'types': ['route']
            },
            {
                'long_name': 'Paris',
                'short_name': 'Paris',
                'types': ['locality', 'political']
            },
            {
                'long_name': 'Paris',
                'short_name': 'Paris',
                'types': ['administrative_area_level_2', 'political']
            },
            {
                'long_name': 'Île-de-France',
                'short_name': 'Île-de-France',
                'types': ['administrative_area_level_1', 'political']
            },
            {
                'long_name': 'France',
                'short_name': 'FR',
                'types': ['country', 'political']
            },
            {
                'long_name': '75007',
                'short_name': '75007',
                'types': ['postal_code']
            }
        ],
        'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
        'geometry': {
            'location': {'lat': 48.85837009999999, 'lng': 2.2944813},
            'location_type': 'ROOFTOP',
            'viewport': {
                'northeast': {'lat': 48.8597190802915, 'lng': 2.295830280291502},
                'southwest': {'lat': 48.8570211197085, 'lng': 2.293132319708498}
                }
            },
        'place_id': 'ChIJLU7jZClu5kcR4PcOOO6p3I0',
        'plus_code': {
            'compound_code': 'V75V+8Q Paris, France',
            'global_code': '8FW4V75V+8Q'
            }, 'types': ['establishment', 'point_of_interest', 'premise']
        }
    ]


data_list_2 = [
    {
        'address_components': [
            {
                'long_name': 'Statue of Liberty National Monument',
                'short_name': 'Statue of Liberty National Monument',
                'types': ['establishment', 'park', 'point_of_interest']
            },
            {
                'long_name': 'Manhattan',
                'short_name': 'Manhattan',
                'types': ['political', 'sublocality', 'sublocality_level_1']
            },
            {
                'long_name': 'New York',
                'short_name': 'New York',
                'types': ['locality', 'political']
            },
            {
                'long_name': 'New York County',
                'short_name': 'New York County',
                'types': ['administrative_area_level_2', 'political']
            },
            {
                'long_name': 'New York',
                'short_name': 'NY',
                'types': ['administrative_area_level_1', 'political']
            },
            {
                'long_name': 'United States',
                'short_name': 'US',
                'types': ['country', 'political']
            },
            {
                'long_name': '10004',
                'short_name': '10004',
                'types': ['postal_code']
            }
        ],
        'formatted_address': 'Statue of Liberty National Monument, New York, NY 10004, USA',
        'geometry': {
            'location': {'lat': 40.6892494, 'lng': -74.04450039999999},
            'location_type': 'GEOMETRIC_CENTER',
            'viewport': {
                'northeast': {'lat': 40.6905983802915, 'lng': -74.04315141970848},
                'southwest': {'lat': 40.6879004197085, 'lng': -74.04584938029149}
            }
        },
        'place_id': 'ChIJPTacEpBQwokRKwIlDXelxkA',
        'plus_code': {
            'compound_code': 'MXQ4+M5 New York, United States',
            'global_code': '87G7MXQ4+M5'
        },
        'types': ['establishment', 'park', 'point_of_interest']
        }
    ]


def test_set_keyword(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    locater._keyword = keyword
    def fake_geocode():
        return data_list_1
    
    monkeypatch.setattr("grandpy.locater.googlemaps.Client.geocode", fake_geocode)
    assert locater._keyword == keyword


def test_get_address():
    locater = loc.Locater()
    locater._result = data_list_2
    assert locater.get_address() == (
        'Statue of Liberty National Monument, New York, NY 10004, USA'
    )


def test_get_latitude():
    locater = loc.Locater()
    locater._result = data_list_2
    assert locater.get_latitude() == 40.6892494


def test_get_longitude():
    locater = loc.Locater()
    locater._result = data_list_2
    assert locater.get_longitude() == -74.04450039999999
