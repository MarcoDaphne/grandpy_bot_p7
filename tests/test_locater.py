#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import pytest

import grandpy.locater as loc


data_list_empty = []
data_list = [
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


def test_set_keyword(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    def fake_geocode(self, question):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )
    locater.set_keyword(keyword)
    assert locater._keyword == keyword


def test_get_address(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    def fake_geocode(self, question):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )
    locater.set_keyword(keyword)
    assert locater.get_address() == (
        'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France'
    )


def test_get_location(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    def fake_geocode(self, question):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )
    locater.set_keyword(keyword)
    assert locater.get_location() == [
        48.85837009999999,
        2.2944813
    ]


def test_get_address_failed(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    def fake_geocode(self, question):
        return data_list_empty
    
    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )
    locater.set_keyword(keyword)
    assert locater.get_address() == None


def test_get_location_failed(monkeypatch):
    keyword = 'tour eiffel'
    locater = loc.Locater()
    def fake_geocode(self, question):
        return data_list_empty
    
    monkeypatch.setattr(
        "grandpy.locater.googlemaps.Client.geocode",
        fake_geocode
    )
    locater.set_keyword(keyword)
    assert locater.get_location() == [None, None]
