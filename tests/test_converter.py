from unittest import TestCase

__author__ = 'smcho'

from simulationAnalyzer import Reader as S
from simulationAnalyzer import Converter as C

class TestConverter(TestCase):

    def setUp(self):
        self.s = S("unittest", "SimpleShareLogic", "b")
        self.p = C(self.s)

    def test_hotToGroup(self):
        self.assertTrue(1 == self.p.hostToGroup(0))
        self.assertTrue(2 == self.p.hostToGroup(1))
        self.assertTrue(3 == self.p.hostToGroup(56))

    def test_hostToGroupID(self):
        self.assertTrue('v' == self.p.hostToGroupID(0))
        self.assertTrue('s' == self.p.hostToGroupID(1))
        self.assertTrue('p' == self.p.hostToGroupID(56))
        self.assertTrue('ma' == self.p.hostToGroupID(81))

    # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
    def test_hostToGroupIDIndex(self):
        self.assertTrue(('v', 1) == self.p.hostToGroupIDIndex(0)) # previous (0)
        self.assertTrue(('s', 1) == self.p.hostToGroupIDIndex(1))
        self.assertTrue(('p', 16) == self.p.hostToGroupIDIndex(56)) # previous 41, 56 - 41 = 15, 15 + 1 == 16
        self.assertTrue(('ma', 1) == self.p.hostToGroupIDIndex(81)) # previous (81), host(81) - previous + 1

    def test_groupIDIndexToHost(self):
        self.assertTrue(self.p.groupIDIndexToHost('v', 1) == 0) # previous (0)
        self.assertTrue(self.p.groupIDIndexToHost('s', 1) == 1)
        self.assertTrue(self.p.groupIDIndexToHost('p', 16) == 56) # previous 41, 56 - 41 = 15, 15 + 1 == 16
        self.assertTrue(self.p.groupIDIndexToHost('ma', 1) == 81) # previous (81), host(81) - previous + 1

        self.assertEqual(1, self.p.hostToGroup(self.p.groupIDIndexToHost("v", 1)))
        self.assertEqual(2, self.p.hostToGroup(self.p.groupIDIndexToHost("s", 1)))
        self.assertEqual(2, self.p.hostToGroup(self.p.groupIDIndexToHost("s", 40)))

        with self.assertRaises(Exception) as context:
            self.p.groupIDIndexToHost("s", 41)
            self.assertTrue("Out of range" in context.exception)

    ###

    def test_contextToGroupIDIndex(self):
        self.assertEqual(("v", 1), self.p.contextToGroupIDIndex("g1c0b"))
        self.assertEqual(("p", 29), self.p.contextToGroupIDIndex("g3c69l")) # 3rd group -> "p", prev 41, 69-41 = 28, 28+1 == 29

    def test_groupIDIndexToContext(self):
        self.assertEqual("g2c1", self.p.groupIDIndexToContext("s", 1))
        self.assertEqual("g2c40", self.p.groupIDIndexToContext("s", 40))

        self.assertEqual("g1c0", self.p.groupIDIndexToContext("v", 1))
        self.assertEqual("g3c69", self.p.groupIDIndexToContext("p", 29))

