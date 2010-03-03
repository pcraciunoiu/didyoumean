# -*- coding: utf-8 -*-

from nose.tools import eq_, assert_not_equal

from didyoumean import DidYouMean


d = DidYouMean('hi-IN')


def test_hindi_sentence():
    """A Hindi sentence with misspelled words should return False"""
    a = u'यह एक समसा ही'
    eq_(False, d.check(a))


def test_good_hindi_sentence():
    """A Hindi sentence with no misspelled words should return True"""
    eq_(True, d.check(u'यह एक समस्या है'))


def test_hindi_correction():
    """Verify that a Hindi sentence is corrected"""
    wrong = u'यह एक समसा ही'
    right = u'यह एक समस्या है'
    corrected = d.suggest(wrong)
    new = u' '.join([word.new for word in corrected])
    assert_not_equal(right, new)
