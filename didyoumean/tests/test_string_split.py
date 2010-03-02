from nose.tools import eq_

from didyoumean import DidYouMean


def test_split_english_sentence():
    d = DidYouMean('en-US')
    words = 'this is a test'
    result = ['this', 'is', 'a', 'test']
    eq_(result, d._split_string(words))


def test_split_french_sentence():
    d = DidYouMean('fr-FR')
    words = "c'est une d'example"
    result = ["c'est", 'une', "d'example"]
    eq_(result, d._split_string(words))
