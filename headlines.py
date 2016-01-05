# -*- coding: utf-8 -*-
import sys
import re
import logging
logger = logging.getLogger(__name__)

"""
headlines
~~~~~~~~~~~~~~~~~
Main module; where the action is.
"""
def articles_to_lower_case(title_str):
    lowercase_words = {u'A':u'a', u'An':u'an', u'And':u'and', 
                        u'As':u'as', u'At':u'at', u'But':u'but',
                        u'By':u'by', u'En':u'en', u'For':u'for',
                        u'If':u'if', u'In':u'in', u'Of':u'of', 
                        u'On':u'on', u'Or':u'or', u'The':u'the',
                        u'To':u'to', u'V':u'v', u'V.':u'v.', 
                        u'Via':u'via', u'Vs':u'vs', u'Vs.':u'vs.'}
    for key,val in lowercase_words.iteritems():
        title_str = title_str.replace(key, val)
    return title_str

def capitalize_first_word(title_str):
    if len(title_str) > 0:
        return u"" + title_str[0].upper() + title_str[1:]
    else:
        return u""

def capitalize_words(title_str):
    return re.sub(
        r"\b('?[a-z])",
        lambda match: match.group(1).capitalize(), title_str)

def titleize(title_str):
    if not isinstance(title_str, unicode):
        raise TypeError('Need to input a unicode string.')
    #titleized = title_str.title()
    capitalized = capitalize_words(title_str)
    return articles_to_lower_case(capitalized)
