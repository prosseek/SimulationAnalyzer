from unittest import TestCase
from simulationAnalyzer import *


__author__ = 'smcho'

testName = "unittest"
class TestGetConfigurationFile(TestCase):
    def test_getResultFile(self):
        self.assertTrue(getResultFile(testName, "SimpleShareLogic", "b").endswith("{}/results/result_smcho.SimpleShareLogic_b.json".format(testName)))
    def test_getConfigurationFile(self):
        self.assertTrue(getConfigurationFile(testName).endswith("{}/c.txt".format(testName)))

    def test_parseConfigurationFile(self):
        res = parseConfigurationFile(testName)
        self.assertTrue(len(res) == 48)