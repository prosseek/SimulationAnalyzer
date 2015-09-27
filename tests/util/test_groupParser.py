from unittest import TestCase

from simulationAnalyzer.util.groupsParser import *

__author__ = 'smcho'


class TestGroupParser(TestCase):
    def setUp(self):
        self.g = GroupParser("unittest", "SimpleShareLogic", "unittest")

    def test_createGroupToGroupIDMap(self):
        m = self.g.groupToGroupIDMap
        expected = {1: 'v', 2: 's', 3: 'p', 4: 'ma', 5: 'mb', 6: 'mc', 7: 'md'}
        self.assertEqual(m, expected)

    def test_createGroupIdCountList(self):
        self.assertEqual(self.g.createGroupIdCountList(),
                         [('v', 1), ('s', 40), ('p', 40), ('ma', 1), ('mb', 1), ('mc', 1), ('md', 1)])

    def test_createGroupIdAccList(self):
        self.assertEqual(self.g.createGroupIdAccList(),
                         [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)])

    def test_getGroupCount(self):
        self.assertEqual(self.g.getGroupCount(), 7)


    def test_getHostCount(self):
        self.assertEqual(self.g.getHostCount(), 85)

