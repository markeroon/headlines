# -*- coding: utf-8 -*-
import sys
import logging
logger = logging.getLogger(__name__)

"""
headlines
~~~~~~~~~~~~~~~~~
Main module; where the action is.
"""

def titleize(title_str):
    if not isinstance(title_str, unicode):
        raise TypeError('Need to input a unicode string.')
    return title_str.title()
