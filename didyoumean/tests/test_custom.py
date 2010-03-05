import os

from nose.tools import eq_

from didyoumean import DidYouMean

ROOT = os.path.abspath(os.path.dirname(__file__))
path = lambda *a: os.path.join(ROOT, *a)

d = DidYouMean('en-US', words=path('words.txt'))


def test_custom_wordlist():
    """Words in the custom word list should be accepted."""
    eq_(True, d.check('facebook'))


def test_custom_wordlist_not():
    """Words not in the custom word list are still wrong."""
    eq_(False, d.check('fireblix'))


def test_custom_wordlist_suggestion():
    """Suggestions should include custom words."""
    eq_('facebook', d.suggest('faecbook')[0].new)


def test_custom_wordlist_case():
    """Ideally, the custom wordlist should be case-insensitive."""
    eq_(True, d.check('Facebook'))
    eq_(True, d.check('FACEBOOK'))
