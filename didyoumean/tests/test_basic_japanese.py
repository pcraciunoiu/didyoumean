from nose.tools import eq_

from didyoumean import DidYouMean


d = DidYouMean('ja-JP')


def test_no_test_japanese():
    """Could not find ja-JP dictionaries, should always return true"""
    eq_(True, d.check('not japanese'))
