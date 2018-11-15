#!/usr/bin/env python3
# Coding: utf-8

import pytest

import grandpy.storyteller as stell


data_list_empty = []
data_list = [
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


def test_location(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    lat = 48.85837009999999
    lng = 2.2944813
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    location = (
        storyteller._latitude,
        storyteller._longitude
    )
    assert location == (lat, lng)


def test_location_failed(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    lat = None
    lng = None
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    location = (
        storyteller._latitude,
        storyteller._longitude
    )
    assert location == (lat, lng)


def test_set_position(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    lat = 48.85837009999999
    lng = 2.2944813
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    assert storyteller._response == data_list


def test_set_position_failed(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list_empty
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    lat = None
    lng = None
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    assert storyteller._response == data_list_empty


def test_choice_title(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list

    def fake_random(self):
        return 'Tour Eiffel'
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    monkeypatch.setattr(
        "grandpy.storyteller.random.choice",
        fake_random
    )
    lat = 48.85837009999999
    lng = 2.2944813
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    assert storyteller.choice_title() == 'Tour Eiffel'


def test_get_informations(monkeypatch):
    class FakePage:
        url = "url Wikipédia"
        summary = "resumé Wikipédia"

    def fake_page(self, title):
        return FakePage()

    def fake_geosearch(self, latitude, longitude):
        return data_list
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )   
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.page",
        fake_page
    )
    storyteller = stell.StoryTeller()
    lat = 48.85837009999999
    lng = 2.2944813
    storyteller.set_position(lat, lng)
    result = storyteller.get_informations()
    assert result == [FakePage.summary, FakePage.url]


def test_get_informations_failed(monkeypatch):
    def fake_geosearch(self, latitude, longitude):
        return data_list_empty
    
    monkeypatch.setattr(
        "grandpy.storyteller.MediaWiki.geosearch",
        fake_geosearch
    )
    lat = None
    lng = None
    storyteller = stell.StoryTeller()
    storyteller.set_position(lat, lng)
    storyteller.get_informations()
    assert storyteller.get_informations() == [None, None]
