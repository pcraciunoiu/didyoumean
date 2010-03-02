from collections import namedtuple
import re

import hunspell


class DidYouMean:
    """
    Checks to see that each word in a string is spelled correctly and, if not,
    provides suggestions for those words.
    """

    def __init__(self, locale):
        """Requires a locale to work correctly."""

        pass


    def check(self, string):
        """Checks to see if the words in this string are spelled correctly."""
        pass


    def suggest(self, string):
        """Returns a list of named tuples with corrections made."""

        Word = namedtuple('Word', 'old new corrected')

        

    def _split_string(self, string):
        """Split a string into component words"""

        wb = re.compile(r'\W', re.UNICODE)
        words = re.split(wb, string)

        return [word.strip() for word in words if word.strip()]
