from unittest import TestCase

__author__ = 'smcho'

from simulationAnalyzer import Reader as R
from simulationAnalyzer import GroupParser as GP
from simulationAnalyzer import SingleAnalyzer as A
from simulationAnalyzer.util.utility import *

from util.testUtils import *

class TestSingleAnalyzer(TestCase):
    def setUp(self):

        simulationName = "unittest"
        strategy = "SimpleShareLogic"
        id = "fixed"

        r = R(simulationName, strategy, id)
        self.gp = GP(simulationName, strategy, id)

        m = {
            'endTime': 5000,
            'iteration': 1,
            'maxIteration':2,
            'summaryType':'b',
            'transmitRange': 50
        }
        results = r.get(m)
        result = results[0]

        self.a = A(self.gp, result)

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

        res2 = self.a.toGroupNameCount(res1)
        count = 0
        for r in res2:
            for j in listToCountList(r):
                count += 1
        self.assertEqual(count, 50)

    def test_showTime(self):
        # [8115.7, 8398.18, 8896.23]
        # [3547.41, 5162.04, 5233.88, 7279.64]
        # [4238.11, 4384.16, 6878.71, 8805.98, 9857.51]
        #print self.a.showTime("v", 1, "ma", 1)
        #print self.a.showTime("ma", 1, "v", 1)
        self.assertEqual(self.a.showTime("v", 1, "ma", 1) , [8115.7, 8398.19, 11277.27])
        self.assertEqual(self.a.showTime("ma", 1, "v", 1) , [5162.04, 7279.64, 10154.13, 13720.45])
        self.assertEqual(self.a.showTime("s", 1, "v", 1)[0] , 4238.11)

    def test_getAllMembers(self):
        count = 0
        for j in self.a.getAllMembers():
            count += 1
        self.assertEqual(count, self.gp.getHostCount())

    def test_getCoveragePercentage(self):
        self.assertEqual(self.a.getCoveragePercentage('v',1),
                        ('g1c0', 4562.5636904761905, 100.0, 84, 84))
        self.assertEqual(self.a.getCoveragePercentage('p',1) ,
                        ('g3c41', 8292.57073529412, 80.95238095238095, 68, 84))
        self.assertEqual(self.a.getCoveragePercentage('ma',1) ,
                        ('g4c81', 7291.358253968254, 75.0, 63, 84))
        self.assertEqual(self.a.getCoveragePercentage('mb',1) ,
                        ('g5c82', 7511.417454545453, 65.47619047619048, 55, 84))
