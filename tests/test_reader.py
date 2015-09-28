import os

from unittest import TestCase
from simulationAnalyzer import Reader as R

__author__ = 'smcho'

testName = "unittest"

class TestReader(TestCase):
    def setUp(self):
        self.r = R("unittest", "SimpleShareLogic", "unittest")

    def test_get(self):
        m = {
            'endTime': 5000,
            'iteration': 2,
            'maxIteration':2,
            'summaryType':'b',
            'transmitRange': 50
        }

        r = self.r.get(m)

        self.assertTrue(len(r) == 1)
        result = r[0]

        self.assertTrue(len(result.getHostToTuplesMap()) == 83)
        self.assertTrue(len(result.getSummaries()) == 85)

    def test_get2(self):
        # There is no 'iteration' element, so all the iterations will be selectd
        m = {
            'endTime': 5000,
            'maxIteration':2,
            'summaryType':'b',
            'transmitRange': 50
        }

        r = self.r.get(m)
        self.assertTrue(len(r) == 2)
        result = r[0]
        self.assertTrue(len(result.getHostToTuplesMap()) == 83)
        self.assertTrue(len(result.getSummaries()) == 85)