# -*- coding: utf-8 -*-

from nose.tools import eq_

from didyoumean import DidYouMean

d = DidYouMean('he-IL')


def test_split_hebrew():
    """Split a Hebrew string (RTL)"""
    phrase = u"ברוך אתה ה' א‑לוהינו מלך העולם"
    words = [u'ברוך', u'אתה', u"ה'", u'א‑לוהינו', u'מלך', u'העולם']
    eq_(words, d._split_string(phrase))


def test_good_hebrew_word():
    """Check the Hebrew word העולם """
    eq_(True, d.check(u'העולם'))


def test_good_hebrew_sentence():
    """Check the Hebrew sentence 'שלום עולם'"""
    eq_(True, d.check(u'שלום עולם'))


def test_bad_hebrew_sentence():
    """Correct the phrase 'שלום עולם'"""
    bad = u'שׂלום עולם'
    good = u'שלום עולם'
    new = u' '.join([w.new for w in d.suggest(bad)])
    eq_(good, new)
