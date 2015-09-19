import os

from unittest import TestCase
from simulationAnalyzer import Reader as S

__author__ = 'smcho'

testName = "unittest"

class TestSimulationAnalyzer(TestCase):

    def setUp(self):
        self.p = S("unittest", "SimpleShareLogic", "b")

    def test_jsonMap(self):
        j = self.p.jsonMap
        self.assertEqual(len(j['hostToTuplesMap']), 84)
        self.assertEqual(len(j['summaries']), 85)

    def test_createGroupToGroupIDMap(self):
        m = self.p.groupToGroupIDMap
        expected = {1: 'v', 2: 's', 3: 'p', 4: 'ma', 5: 'mb', 6: 'mc', 7: 'md'}
        self.assertEqual(m, expected)

