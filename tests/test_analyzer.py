from unittest import TestCase

__author__ = 'smcho'


from simulationAnalyzer import Reader as R
from simulationAnalyzer import Converter as C
from simulationAnalyzer import Analyzer as A
from simulationAnalyzer import utility as u

class TestAnalyzer(TestCase):

    def setUp(self):
        self.s = R("unittest", "SimpleShareLogic", "b")
        self.c = C(self.s)
        self.a = A(self.c)

    def test_getContext(self):
        # Check what the v1 has
        res1 = self.a.getContexts("v", 1)
        res2 = self.a.toContextNames(res1)
        for r in res2:
            print u.listToCountList(r)

    def test_showTime(self):
        print self.a.showTime("v",1,"ma",1)
        print self.a.showTime("ma",1, "v", 1)
        print self.a.showTime("s",1, "v", 1)

