from collections import namedtuple
import re
from os import path

import hunspell

from encoding import force_unicode


class DidYouMean(object):
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

        words = self._split_string(string)

        if self.hunspell is None:
            """If I don't have a dictionary, just assume everything is fine"""
            return True

        for word in words:
            if not self.hunspell.spell(word.encode('utf-8')):
                return False

        return True


    def suggest(self, string):
        """Returns a list of named tuples with corrections made."""

        Word = namedtuple('Word', 'old new corrected')

        if self.hunspell is None:
            result = []
            for word in self._split_string(string):
                result.append(Word(word, word, False))
            return result

        result = []
        for word in self._split_string(string):
            if not self.hunspell.spell(word.encode('utf-8')):
                try:
                    new = self.hunspell.suggest(word.encode('utf-8'))[0]
                    result.append(Word(word, new.decode('utf-8'), True))
                except IndexError:
                    result.append(Word(word, word, False))
            else:
                result.append(Word(word, word, False))

        return result


    def _split_string(self, string):
        """Split a string. I'm wrapping this just in case I need to do 
        something fancier."""

        return string.split()
