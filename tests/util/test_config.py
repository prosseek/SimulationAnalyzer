import os

from unittest import TestCase
from simulationAnalyzer.util.config import *
from testUtils import *

__author__ = 'smcho'

class TestConfig(TestCase):
    def test_read(self):
        filePath = getTestResourceDirectory() + "hello.txt"
        p = Config()
        result = p.readConfigurationFile(filePath)
        self.assertEqual(49, len(result))
        self.assertEqual(result['Group4.worldSize'],[5000, 5000])