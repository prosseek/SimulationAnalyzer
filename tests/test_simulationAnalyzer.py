import os

from unittest import TestCase
from simulationAnalyzer import SimulationAnalyzer as S
from simulationAnalyzer import getResultFile

__author__ = 'smcho'

testName = "unittest"

class TestSimulationAnalyzer(TestCase):
    def setUp(self):
        self.p = S("unittest", "SimpleShareLogic", "b")
    def test_simulationAnalyzer(self):
        line = self.p.dict

    def test_idToGroup(self):
        self.assertTrue(1 == self.p.hostToGroup(0))
        self.assertTrue(2 == self.p.hostToGroup(1))
        self.assertTrue(3 == self.p.hostToGroup(56))

    def test_groupToId(self):
        self.assertEqual(1, self.p.hostToGroup(self.p.groupIdToHost("v", 1)))
        self.assertEqual(2, self.p.hostToGroup(self.p.groupIdToHost("s", 1)))
        self.assertEqual(2, self.p.hostToGroup(self.p.groupIdToHost("s", 40)))

        with self.assertRaises(Exception) as context:
            self.p.groupIdToHost("s", 41)
            self.assertTrue("Out of range" in context.exception)

        #print self.p.idToGroup(self.p.groupToId("s", 41))
        self.assertEqual(3, self.p.hostToGroup(self.p.groupIdToHost("p", 1)))
        self.assertEqual(3, self.p.hostToGroup(self.p.groupIdToHost("p", 40)))
        self.assertEqual(4, self.p.hostToGroup(self.p.groupIdToHost("ma", 1)))
        self.assertEqual(5, self.p.hostToGroup(self.p.groupIdToHost("mb", 1)))
        self.assertEqual(6, self.p.hostToGroup(self.p.groupIdToHost("mc", 1)))
        self.assertEqual(7, self.p.hostToGroup(self.p.groupIdToHost("md", 1)))

    def test_getContext(self):
        # print self.p.dict
        print self.p.getContexts("v",1)
        print self.p.getContexts("ma",1)
        print self.p.getContexts("mb",1)
        print self.p.getContexts("mc",1)
        print self.p.getContexts("md",1)

