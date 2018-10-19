#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

from mediawiki import MediaWiki

import grandpy.parser as pars
import grandpy.locater as pos


class Storyteller:
    """docstring"""
    def __init__(self, keyword, position):
        self.keyword = keyword
        self.position = position
        self.wikipedia = MediaWiki()

    def search_position_data(self):
        """docstring"""
        return self.wikipedia.geosearch(
            latitude=self.position.latitude,
            longitude=self.position.longitude
        )

    def show_data(self):
        search = self.search_position_data()
        print(search)


if __name__ == "__main__":
    question = pars.Parser()
    question.set_question("Où puis-je trouver une pizzeria à LONGJUMEAU ?")
    question.remove_accents()
    question.remove_punctuations()
    question.remove_current_word()
    position = pos.Locater(question)
    position.get_latitude()
    position.get_longitude()
    story = Storyteller(question, position)
    story.search_position_data()
    story.show_data()