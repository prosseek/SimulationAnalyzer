import os

from unittest import TestCase
from simulationAnalyzer import Reader as R
from simulationAnalyzer.util.path import *

__author__ = 'smcho'

testName = "unittest"


class TestReader(TestCase):
    def setUp(self):
        self.r = R("unittest", "SimpleShareLogic", "b", getBaseDirectory())

    def test_jsonMap(self):
        j = self.r.jsonMap
        self.assertEqual(len(j['hostToTuplesMap']), 84)
        self.assertEqual(len(j['summaries']), 85)

    def test_createGroupToGroupIDMap(self):
        m = self.r.groupToGroupIDMap
        expected = {1: 'v', 2: 's', 3: 'p', 4: 'ma', 5: 'mb', 6: 'mc', 7: 'md'}
        self.assertEqual(m, expected)

    def test_createGroupIdCountList(self):
        self.assertEqual(self.r.createGroupIdCountList(),
                         [('v', 1), ('s', 40), ('p', 40), ('ma', 1), ('mb', 1), ('mc', 1), ('md', 1)])

    def test_createGroupIdAccList(self):
        self.assertEqual(self.r.createGroupIdAccList(),
                         [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)])

    def test_getGroupCount(self):
        self.assertEqual(self.r.getGroupCount(), 7)


    def test_getHostCount(self):
        self.assertEqual(self.r.getHostCount(), 85)
