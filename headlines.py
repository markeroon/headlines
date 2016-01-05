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

def capitalize_words(title_str):
    return re.sub(
        r"\b('?[a-z])",
        lambda match: match.group(1).capitalize(), title_str)

def titleize(title_str):
    lowercase_words = [ u'a' u'an' u'and' u'as' u'at' u'but' u'by' 
                        u'en' u'for' u'if' u'in' u'of' u'on' u'or'
                        u'the' u'to' u'v' u'v.' u'via' u'vs' u'vs.']
    if not isinstance(title_str, unicode):
        raise TypeError('Need to input a unicode string.')
    #titleized = title_str.title()
    capitalized = capitalize_words(title_str)
    return capitalized    
