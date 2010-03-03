didyoumean
==========

didyoumean is a spelling-suggestion wrapper for pyhunspell designed to offer
suggestions for misspelled words in search engine results, eg::

    Did you mean: ... ?


Requirements
------------

didyoumean requires two things: ``pyhunspell``, which, unfortunately, is not 
on PyPI, and Hunspell/MySpell dictionaries. The dictionaries can be installed
via whatever package manager is available on your system.


Installing ``pyhunspell``
^^^^^^^^^^^^^^^^^^^^^^^^^

Using pip_::

    pip install -e svn+http://pyhunspell.googlecode.com/svn/trunk/#egg=pyhunspell

In turn, ``pyhunspell`` requires hunspell, obviously.

.. _pip: http://pypi.python.org/pypi/pip


Usage
-----

All you need to do is create a ``DidYouMean`` object with the correct locale,
then use the ``check()`` or ``suggest()`` methods.::

    >>> d = DidYouMean('en-US')

    >>> d.check('this sentence is correct')
    True

    >>> d.check('this sentence is worng')
    False

    >>> d.suggest('this sentence is worng')
    [Word(old='this', new='this', corrected=False),
    Word(old='sentence', new='sentence', corrected=False),
    Word(old='is', new='is', corrected=False),
    Word(old='worng', new='wrong', corrected=True)]

For each word in a sentence, ``suggest()`` returns a ``Word`` named tuple,
with three properties: ``old`` (the original word), ``new`` (the new word),
and ``corrected`` (a boolean, basically ``not old == new``).

There is an optional ``dict_dir`` argument to ``DidYouMean()`` which tells it
where to look for dictionary files. By default, it is ``/usr/share/myspell/``.
You should include a trailing slash.


Fallback for unsupported locales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should always try to use a full locale (with country) when possible.
didyoumean will fall back to just a language if it has to, but in many cases,
only locale-specific dictionaries exist (like English).

For example, if I attempt to use the locale ``wx-YZ``, didyoumean will do the
following::

    if wx_YZ dict exists
        use wx_YZ
    else if wx dict exists
        use wx
    else
        check() always returns True

If didyoumean can't find any dictionary, ``check()`` always returns true, and
``suggest()`` will always return words with no corrections. This is to avoid
marking correctly spelled words as incorrect, just because a dictionary can't
be found, and is motivated by the search engine use-case. (You do not want to
offer spelling suggestions when you can't check spelling for a locale.)


A note on English
^^^^^^^^^^^^^^^^^

Unfortunately, as far as I can tell, MySpell does not have a generic English
dictionary. You need to specify ``en-US``, ``en-GB``, vel c. If you find a
generic ``en`` dictionary, please let me know!


Limitations
-----------

As with most spell-checks, didyoumean will not work on languages without
separators between words. (I couldn't find dictionaries for Japanese or
Chinese.) Since didyoumean works by checking each word individually,
languages without word separators break.
