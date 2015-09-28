from unittest import TestCase
from simulationAnalyzer.util.name import *

__author__ = 'smcho'

d = {
    "transmitRange":50,
    "endTime":10000,
    "iteration":1
}
expected = "endTime_10000!iteration_1!transmitRange_50"

d2 = {
    "transmitRange":50,
    "endTime":10000,
    "iteration":1
}
resultFile = "../hello/b-3!endTime_5000!iteration_2!transmitRange_50.json"
resultFileWrongFormat = "../hello/b!endTime_5000!iteration_2!transmitRange_50.json"

class TestName(TestCase):
    def test_dictToName(self):
        self.assertEqual(expected, Name.dictToName(d))

    def test_nameToDict(self):
        self.assertEqual(Name.nameToDict(expected), d)

    def test_resultFilePathToDictExpectException(self):
        with self.assertRaises(Exception) as context:
            Name.resultFilePathToDict(resultFileWrongFormat)
        self.assertTrue("Format error" in str(context.exception))

    def test_resultFilePathToDict(self):
        self.assertEqual(Name.resultFilePathToDict(resultFile),
                        {'summaryType': 'b', 'transmitRange': 50, 'endTime': 5000, 'iteration': 2, 'maxIteration':3})

    def test_dictToResultFilePath(self):
        input =  {'summaryType': 'b', 'transmitRange': 50, 'endTime': 5000, 'iteration': 2, 'maxIteration':3}
        expected = "b-3!endTime_5000!iteration_2!transmitRange_50.json"
        self.assertEqual(Name.dictToResultFilePath(input), expected)