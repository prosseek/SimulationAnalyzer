from unittest import TestCase

from simulationAnalyzer.util.path import *
from simulationAnalyzer.json_result import *

__author__ = 'smcho'

class TestJSONResult(TestCase):
    def setUp(self):
        self.p = Path("unittest", "SimpleShareLogic","unittest")
        filePath = self.p.getResultDirectory() + "b-2!endTime_5000!iteration_2!transmitRange_50.json"
        self.jsonResult = JSONResult(filePath)

    # This is not necessary
    #
    # def test_loadJSON(self):
    #     self.jsonResult.loadJSON()


    def test_getHostToTuplesMap(self):
        self.assertEqual(len(self.jsonResult.getHostToTuplesMap()), 83)

    def test_getSummaries(self):
        self.assertEqual(len(self.jsonResult.getSummaries()), 85)


