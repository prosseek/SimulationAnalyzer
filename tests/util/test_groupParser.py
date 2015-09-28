from unittest import TestCase

from simulationAnalyzer.util.group_parser import *

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

    def test_hotToGroup(self):
        self.assertTrue(1 == self.g.hostToGroup(0))
        self.assertTrue(2 == self.g.hostToGroup(1))
        self.assertTrue(3 == self.g.hostToGroup(56))

    def test_hostToGroupID(self):
        self.assertTrue('v' == self.g.hostToGroupID(0))
        self.assertTrue('s' == self.g.hostToGroupID(1))
        self.assertTrue('p' == self.g.hostToGroupID(56))
        self.assertTrue('ma' == self.g.hostToGroupID(81))

    # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
    def test_hostToGroupIDIndex(self):
        self.assertTrue(('v', 1) == self.g.hostToGroupIDIndex(0)) # previous (0)
        self.assertTrue(('s', 1) == self.g.hostToGroupIDIndex(1))
        self.assertTrue(('p', 16) == self.g.hostToGroupIDIndex(56)) # previous 41, 56 - 41 = 15, 15 + 1 == 16
        self.assertTrue(('ma', 1) == self.g.hostToGroupIDIndex(81)) # previous (81), host(81) - previous + 1

    def test_groupIDIndexToHost(self):
        self.assertTrue(self.g.groupIDIndexToHost('v', 1) == 0) # previous (0)
        self.assertTrue(self.g.groupIDIndexToHost('s', 1) == 1)
        self.assertTrue(self.g.groupIDIndexToHost('p', 16) == 56) # previous 41, 56 - 41 = 15, 15 + 1 == 16
        self.assertTrue(self.g.groupIDIndexToHost('ma', 1) == 81) # previous (81), host(81) - previous + 1

        self.assertEqual(1, self.g.hostToGroup(self.g.groupIDIndexToHost("v", 1)))
        self.assertEqual(2, self.g.hostToGroup(self.g.groupIDIndexToHost("s", 1)))
        self.assertEqual(2, self.g.hostToGroup(self.g.groupIDIndexToHost("s", 40)))

        with self.assertRaises(Exception) as context:
            self.g.groupIDIndexToHost("s", 41)
            self.assertTrue("Out of range" in context.exception)

    ###

    def test_contextToGroupIDIndex(self):
        self.assertEqual(("v", 1), self.g.contextToGroupIDIndex("g1c0b"))
        self.assertEqual(("p", 29), self.g.contextToGroupIDIndex("g3c69l")) # 3rd group -> "p", prev 41, 69-41 = 28, 28+1 == 29

    def test_groupIDIndexToContext(self):
        self.assertEqual("g2c1", self.g.groupIDIndexToContext("s", 1))
        self.assertEqual("g2c40", self.g.groupIDIndexToContext("s", 40))

        self.assertEqual("g1c0", self.g.groupIDIndexToContext("v", 1))
        self.assertEqual("g3c69", self.g.groupIDIndexToContext("p", 29))