from unittest import TestCase
from simulationAnalyzer.util.path import *

__author__ = 'smcho'

testName = "unittest"
strategy = "SimpleShareLogic"
contextType = "b"

class TestPath(TestCase):

    def test_getResultFile(self):
        self.assertTrue(getResultFilePath(testName, strategy, contextType).endswith("{}/results/result_smcho.{}_{}.json".format(testName, strategy, contextType)))
    def test_getConfigurationFile(self):
        self.assertTrue(getConfigurationFilePath(testName).endswith("{}/c.txt".format(testName)))
    # def test_parseConfigurationFile(self):
    #     res = readConfigurationFile(testName)
    #     self.assertTrue(len(res) == 48)