from unittest import TestCase

__author__ = 'smcho'


from simulationAnalyzer import Reader as R
from simulationAnalyzer import Converter as C
from simulationAnalyzer import Analyzer as A
from simulationAnalyzer import utility as u

class TestAnalyzer(TestCase):

    def setUp(self):
        self.r = R("unittest", "SimpleShareLogic", "b")
        self.c = C(self.r)
        self.a = A(self.c)

    def test_getContext(self):
        # Check what the v1 has
        res1 = self.a.getContexts("v", 1)
        res2 = self.a.toContextNames(res1)
        for r in res2:
            print u.listToCountList(r)

    def test_showTime(self):
        # [8115.7, 8398.18, 8896.23]
        # [3547.41, 5162.04, 5233.88, 7279.64]
        # [4238.11, 4384.16, 6878.71, 8805.98, 9857.51]
        print self.a.showTime("v",1,"ma",1)
        print self.a.showTime("ma",1, "v", 1)
        print self.a.showTime("s",1, "v", 1)

    def test_getAllMembers(self):
        count = 0
        for j in self.a.getAllMembers():
            count += 1
        self.assertEqual(count, self.r.getHostCount())
