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
    eq_(False, d.check('tset'))


def test_check_invalid_string():
    eq_(False, d.check('this is a tset'))
