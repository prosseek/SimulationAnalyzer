from unittest import TestCase

from simulationAnalyzer import utility

__author__ = 'smcho'


class TestListToCountList(TestCase):
    def test_listToCountList(self):
        print utility.listToCountList(['a'])
        print utility.listToCountList(['a', 'a'])
        print utility.listToCountList(['a', 'a', 'a'])
        print utility.listToCountList(['a','b'])
        print utility.listToCountList(['a','a','b','b'])
        print utility.listToCountList(['a','a','b','b','b'])

