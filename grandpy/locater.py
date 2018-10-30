#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import googlemaps

from .constants import gmaps_key


class Locater:
    """docstring"""

    def __init__(self):
        self.gmaps = googlemaps.Client(key=gmaps_key)
        self._keyword = None
        self._result = None

    def set_keyword(self, keyword):
        """docstring"""
        self._keyword = keyword
        self._result = self.gmaps.geocode(self._keyword)
        print(self._result)

    def get_address(self):
        """docstring"""
        return self._result[0].get('formatted_address')

    def get_latitude(self):
        """docstring"""
        return self._result[0]['geometry']['location'].get('lat')

    def get_longitude(self):
        """docstring"""
        return self._result[0]['geometry']['location'].get('lng')


if __name__ == "__main__":
    place = Locater()
    place.set_keyword("tour eiffel")
    place.get_address()
    place.get_latitude()
    place.get_longitude()
