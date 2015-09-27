import os

from unittest import TestCase
from simulationAnalyzer import Reader as R

__author__ = 'smcho'

testName = "unittest"

class TestReader(TestCase):
    def setUp(self):
        self.r = R("unittest", "SimpleShareLogic", "unittest")

    def test_readAllJSONFiles(self):
        self.r.readAllJSONFiles()
