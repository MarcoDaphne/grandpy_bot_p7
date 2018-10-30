#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

from mediawiki import MediaWiki

import random


class StoryTeller:
    """docstring"""
    def __init__(self):
        self.wikipedia = MediaWiki(lang=u'fr')
        self._response = None
        self.summary = None

    def set_position(self, lat, lng):
        """docstring"""
        self._response = self.wikipedia.geosearch(
            latitude = lat,
            longitude = lng
        )

    def choice_summary(self):
        """docstring"""
        return random.choice(self._response)
    
    def show_summary(self):
        """docstring"""
        self.summary = self.wikipedia.page(self.choice_summary())
        self.summary = self.summary.summary
        print(self.summary)


if __name__ == "__main__":
    story = StoryTeller()
    story.set_position(40.6892494, -74.04450039999999)
    story.show_summary()