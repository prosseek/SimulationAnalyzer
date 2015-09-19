from unittest import TestCase
from simulationAnalyzer import *


__author__ = 'smcho'

testName = "unittest"

class TestGetConfigurationFile(TestCase):

    def test_getResultFile(self):
        self.assertTrue(getResultFilePath(testName, "SimpleShareLogic", "b").endswith("{}/results/result_smcho.SimpleShareLogic_b.json".format(testName)))
    def test_getConfigurationFile(self):
        self.assertTrue(getConfigurationFilePath(testName).endswith("{}/c.txt".format(testName)))
    def test_parseConfigurationFile(self):
        res = readConfigurationFile(testName)
        self.assertTrue(len(res) == 48)