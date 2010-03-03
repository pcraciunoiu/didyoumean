# -*- coding: utf-8 -*-

from nose.tools import eq_, assert_not_equal

from didyoumean import DidYouMean


d = DidYouMean('fa-IR')


def test_farsi_sentence():
    """A Farsi sentence with misspelled words should return False"""
    a = u'ابن یک جملهٔ آرمایسی است'
    eq_(False, d.check(a))


def test_good_farsi_sentence():
    """A Farsi sentence with no misspelled words should return True"""
    eq_(True, d.check(u'این یک جملهٔ آزمایشی است'))


def test_farsi_correction():
    """Verify that a Farsi sentence is corrected"""
    wrong = u'ابن یک جملهٔ آرمایسی است'
    right = u'این یک جملهٔ آزمایشی است'
    corrected = d.suggest(wrong)
    new = u' '.join([word.new for word in corrected])
    assert_not_equal(wrong, new)
