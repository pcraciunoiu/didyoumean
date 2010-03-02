from collections import namedtuple
import re
from os import path

import hunspell


class DidYouMean:
    """
    Checks to see that each word in a string is spelled correctly and, if not,
    provides suggestions for those words.
    """

    def __init__(self, locale, dict_dir='/usr/share/myspell/'):
        """Requires a locale to work correctly."""

        lang, co = re.split(r'\W', locale, 2)
        locale = u'_'.join([lang, co])

        if path.isfile(dict_dir+locale+'.dic'):
            self.hunspell = hunspell.HunSpell(dict_dir+locale+'.dic',
                                              dict_dir+locale+'.aff')
        elif path.isfile(dict_dir+lang+'.dic'):
            self.hunspell = hunspell.HunSpell(dict_dir+lang+'.dic',
                                              dict_dir+lang+'.aff')
        else:
            self.hunspell = None


    def check(self, string):
        """Checks to see if the words in this string are spelled correctly."""

        words = [unicode(word) for word in string.split()]

        if self.hunspell is None:
            """If I don't have a dictionary, just assume everything is fine"""
            return True

        for word in words:
            if not self.hunspell.spell(word):
                return False

        return True


    def suggest(self, string):
        """Returns a list of named tuples with corrections made."""

        Word = namedtuple('Word', 'old new corrected')

        return None
