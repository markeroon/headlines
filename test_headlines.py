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
        tst_str = u"My first post | My"
        assert headlines.titleize(tst_str) == "My First Post | My"
    def test_japanese_chars(self):
        tst_str = u"僰  僱  僲  僳  僴  僵  僶  僷  僸  價 僺  僻  僼  僽  僾  僿"        
        assert headlines.titleize(tst_str) == tst_str
