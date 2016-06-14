"""Test functions from Token module"""
import unittest
from netineti.token import Token

class TestToken(unittest.TestCase):
    """Test token methods"""

    def test_is_tokenizable(self):
        """Checks if a string should be tokenized"""
        #at least one char
        self.assertFalse(Token.is_tokenizable(''))
        self.assertTrue(Token.is_tokenizable(','))
        self.assertTrue(Token.is_tokenizable('|'))
        self.assertTrue(Token.is_tokenizable('a'))
        self.assertTrue(Token.is_tokenizable('a!'))
        self.assertTrue(Token.is_tokenizable('#!$^^%,.'))
        self.assertTrue(Token.is_tokenizable('h?'))
        self.assertTrue(Token.is_tokenizable('?...mm'))

    def test_token(self):
        """Creates Token instance with default accessors"""
        token = Token(0, 4, 'hello!')
        self.assertEqual(token.start, 0)
        self.assertEqual(token.end, 4)
        self.assertEqual(token.verbatim, 'hello!')

    def test_clean(self):
        """Check if token cleans verbatim correctly"""
        words = ["!helo", "helo!", "123abc", "abc123", ",abdcc,adfd.",
                 "#aon", "|sdfs|sdf|", ""]
        tokens = [Token(0, len(w), w) for w in words]
        cleans = [t.cleaned for t in tokens]
        self.assertEqual(cleans, ['helo', 'helo', 'abc', 'abc', 'abdcc,adfd',
                                  'aon', 'sdfs|sdf', ''])
