#!/usr/bin/env python3
# Coding: utf-8

"""docstring"""

import grandpy.parser as pars
import grandpy.locater as loct
import grandpy.storyteller as steller
import grandpy.answer_manager as answer_man

class Answer:
    """docstring"""
    def __init__(self):
        self._answer = {}

    def answer_user_query(self, query):
        parser = pars.Parser()
        locater = loct.Locater()
        storyteller = steller.StoryTeller()
        manage = answer_man.AnswerManager()
        self._answer['Parser'] = manage.check_parser(query)
        parser.set_question(query)
        parser.remove_accents()
        parser.remove_punctuations()
        parser.remove_current_word()
        locater.set_keyword(parser.question)
        self._answer['Locater'] = {
            'say': manage.check_locater(
                locater.get_address(),
                locater.get_location()
            ),
            'data': {
                'address': locater.get_address(),
                'location': locater.get_location()
            }
        }
        storyteller.set_position(
            locater.get_location()[0],
            locater.get_location()[1]
            )
        self._answer['StoryTeller'] = {
            'say': manage.check_storyteller(storyteller.get_informations()),
            'data': {
                'summary': storyteller.get_informations()[0],
                'url': storyteller.get_informations()[1]
            }
        }
        return self._answer


if __name__ == "__main__":
    grandpy = Answer()
    grandpy.answer_user_query("Bonjour GrandPy, où se trouve le rocher du diamant en Martinique ?")