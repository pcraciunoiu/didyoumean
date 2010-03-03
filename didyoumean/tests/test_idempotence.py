from nose.tools import eq_

from didyoumean import DidYouMean

d = DidYouMean('en-US')


def test_idempotent_no_correction():
    a = 'this is a test'
    new = ' '.join([word.new for word in d.suggest(a)])
    eq_(a, new)
    next = ' '.join([word.new for word in d.suggest(new)])
    eq_(a, next)
    eq_(new, next)


def test_idempotent_correction():
    a = 'this is worng'
    new = ' '.join([word.new for word in d.suggest(a)])
    next = ' '.join([word.new for word in d.suggest(new)])
    eq_(new, next)
