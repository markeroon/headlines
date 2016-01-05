#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import headlines

class TestRequests(object):
    def test_one(self):
        with pytest.raises(TypeError):
            tst_str = "My first post | My"
            headlines.titleize(tst_str)
    def test_unicode(self):
        tst_str = u"My Vs. post | My To"
        assert headlines.titleize(tst_str) == "My vs. Post | My to"
    def test_japanese_chars(self):
        tst_str = u"僰  僱  僲  僳  僴  僵  僶  僷  僸  價 僺  僻  僼"
        assert headlines.titleize(tst_str) == tst_str
    def test_capitalize_first_word(self):
        tst_str = u"to the Dregs"
        assert headlines.titleize(tst_str) == "To the Dregs"
    def test_empty_string(self):
        assert headlines.titleize(u"") == u""
