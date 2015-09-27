from unittest import TestCase
from simulationAnalyzer.util.name import *

__author__ = 'smcho'

d = {
    "transmitRange":50,
    "endTime":10000,
    "iteration":1
}
expected = "endTime_10000!iteration_1!transmitRange_50"

class TestName(TestCase):
    def test_dictToName(self):
        self.assertEqual(expected, Name.dictToName(d))

    def test_nameToDict(self):
        self.assertEqual(Name.nameToDict(expected), d)
