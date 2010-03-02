# -*- coding: utf-8 -*-

from nose.tools import eq_

from didyoumean import DidYouMean


d = DidYouMean('fa-IR')


def test_farsi_sentence():
    """A Farsi sentence with misspelled words should return False"""
    eq_(False, d.check(u'ابن یک جملهٔ آرمایسی است'))


def test_farsi_correction():
    """Verify that a Farsi sentence is corrected"""
    wrong = u'ابن یک جملهٔ آرمایسی است'
    right = u'این یک جملهٔ آزمایشی است'
    corrected = d.suggest(wrong)
    new = [word.new for word in corrected]
    new = u' '.join(new)
    eq_(new, right)
