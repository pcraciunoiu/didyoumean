# -*- coding: utf-8 -*-

import re

from nose.tools import eq_

from didyoumean import DidYouMean


def test_split_english_sentence():
    """Split a simple string in English"""
    d = DidYouMean('en-US')
    words = 'this is a test'
    result = ['this', 'is', 'a', 'test']
    eq_(result, d._split_string(words))


def test_split_french_sentence():
    """Split a string in French, which has apostrophes in it"""
    d = DidYouMean('fr-FR')
    words = "c'est une d'example"
    result = ["c'est", 'une', "d'example"]
    eq_(result, d._split_string(words))


def test_split_farsi_sentence():
    """Split a string in Farsi, an RTL language"""
    d = DidYouMean('fa-IR')
    words = u'این یک جملهٔ آزمایشی است'
    result = [u'این', u'یک', u'جملهٔ', u'آزمایشی', u'است']
    eq_(result, d._split_string(words))


def test_split_hindi_sentence():
    """Split a string in Hindi"""
    d = DidYouMean('hi-IN')
    words = u'यह एक नमून है'
    result = [u'यह', u'एक', u'नमून', u'है']
    eq_(result, d._split_string(words))
