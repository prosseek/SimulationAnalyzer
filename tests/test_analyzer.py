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
        # Returns what contexts "v1" has in a group.
        # For v1 (itself), it shows that it receives three times.
        # [('v1', 4)]
        # [('s1', 3), ('s2', 3), ('s3', 4), ('s4', 3), ('s5', 3), ('s6', 3), ('s7', 3), 's8', ('s9', 3), ('s10', 3), ('s11', 3), 's12', ('s13', 3), ('s14', 3), ('s15', 3), ('s16', 2), ('s17', 3), ('s18', 4), ('s19', 3), ('s20', 3), ('s21', 3), ('s22', 3), ('s23', 3), ('s24', 3), ('s25', 3), ('s27', 3), ('s28', 3), ('s29', 3), ('s30', 3), ('s31', 3), ('s32', 4), ('s33', 3), ('s34', 3), ('s35', 3), ('s36', 3), ('s37', 3), ('s38', 3), ('s39', 3), ('s40', 3)]
        # [('p1', 3), ('p2', 3), ('p3', 3), ('p4', 3), ('p5', 3), ('p6', 3), ('p7', 3), ('p8', 3), ('p9', 3), ('p10', 3), ('p11', 3), ('p12', 3), ('p13', 3), ('p14', 3), ('p15', 4), ('p16', 3), ('p17', 3), ('p18', 3), ('p19', 3), ('p20', 3), ('p21', 3), ('p23', 3), 'p24', ('p25', 3), ('p26', 3), ('p27', 3), ('p28', 3), ('p29', 3), ('p30', 3), ('p31', 3), ('p32', 2), ('p33', 3), ('p34', 3), ('p35', 3), ('p36', 3), ('p37', 3), ('p38', 3), ('p39', 3), ('p40', 3)]
        # [('ma1', 3)]
        # [('mb1', 3)]
        # [('mc1', 3)]
        # [('md1', 3)]

        # Check what the v1 has
        res1 = self.a.getContexts("v", 1)
        res2 = self.a.toContextNames(res1)
        count = 0
        for r in res2:
            for j in u.listToCountList(r):
                count += 1
        self.assertEqual(count, 83)

    def test_showTime(self):
        # [8115.7, 8398.18, 8896.23]
        # [3547.41, 5162.04, 5233.88, 7279.64]
        # [4238.11, 4384.16, 6878.71, 8805.98, 9857.51]

        self.assertTrue(self.a.showTime("v", 1, "ma", 1)[0] == 8115.7)
        self.assertTrue(self.a.showTime("ma", 1, "v", 1)[0] == 3547.41)
        self.assertTrue(self.a.showTime("s", 1, "v", 1)[0] == 4238.11)

    def test_getAllMembers(self):
        count = 0
        for j in self.a.getAllMembers():
            count += 1
        self.assertEqual(count, self.r.getHostCount())

    def test_getCoveragePercentage(self):
        self.assertTrue(self.a.getCoveragePercentage('v',1) ==
                        ('g1c0', 4255.369759036144, 98.80952380952381, 83, 84))
        self.assertTrue(self.a.getCoveragePercentage('p',1) ==
                        ('g3c41', 6838.456027397262, 86.90476190476191, 73, 84))
        self.assertTrue(self.a.getCoveragePercentage('ma',1) ==
                        ('g4c81', 5893.044050632911, 94.04761904761905, 79, 84))
        self.assertTrue(self.a.getCoveragePercentage('mb',1) ==
                        ('g5c82', 5861.724177215189, 94.04761904761905, 79, 84))
