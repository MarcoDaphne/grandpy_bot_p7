#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

from mediawiki import MediaWiki

import random


class StoryTeller:
    """docstring"""
    def __init__(self):
        self.wikipedia = MediaWiki(lang=u'fr')
        self._latitude = None
        self._longitude = None
        self._response = None
        self._url = None
        self._summary = None

    def set_position(self, latitude, longitude):
        """docstring"""
        self._latitude = latitude
        self._longitude = longitude
        if self._latitude == None and self._longitude == None:
            self._response = []
        else:
            self._response = self.wikipedia.geosearch(
                latitude=self._latitude,
                longitude=self._longitude
            )

    def choice_title(self):
        """docstring"""
        return random.choice(self._response)
    
    def get_informations(self):
        """docstring"""
        if self._response == []:
            return [self._summary, self._url]
        else:
            page = self.wikipedia.page(self.choice_title())
            self._summary = page.summary
            self._url = page.url
            return [self._summary, self._url]


if __name__ == "__main__":
    story = StoryTeller()
    story.set_position(48.85837009999999, 2.2944813)
    story.get_informations()
