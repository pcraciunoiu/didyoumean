from nose.tools import eq_

from didyoumean import DidYouMean


d = DidYouMean('en-US')


def test_check_valid_word():
    """Make sure a valid single word is accepted."""
    eq_(True, d.check('test'))


def test_check_valid_string():
    """Check that all the valid words in a string are valid."""
    eq_(True, d.check('this is a test'))


def test_check_invalid_word():
    """A signle misspelled word should return false"""
    eq_(False, d.check('tset'))


def test_check_invalid_string():
    """A misspelled word in a sentence should return false"""
    eq_(False, d.check('this is a tset'))


def test_correct_english_sentence():
    """A misspellend word in an English sentence should be corrected"""
    wrong = 'this is worng'
    new = ' '.join([word.new for word in d.suggest(wrong)])
    eq_('this is wrong', new)


def test_wrong_capitalization():
    """Make sure that passing incorrectly capitalized locales still works"""
    e = DidYouMean('en-us')
    eq_(False, e.check('worng'))
