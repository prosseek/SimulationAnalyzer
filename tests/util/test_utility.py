from unittest import TestCase

from simulationAnalyzer.util.utility import *

__author__ = 'smcho'


class TestUtility(TestCase):
    def test_listToCountList(self):
        self.assertTrue(listToCountList(['a']) == ['a'])
        self.assertTrue(listToCountList(['a', 'a']) == [('a', 2)])
        self.assertTrue(listToCountList(['a', 'a', 'a']) == [('a', 3)])
        self.assertTrue(listToCountList(['a','b']) == ['a', 'b'])
        self.assertTrue(listToCountList(['a','a','b','b']) == [('a', 2), ('b', 2)])
        self.assertTrue(listToCountList(['a','a','b','b','b']) == [('a', 2), ('b', 3)])

