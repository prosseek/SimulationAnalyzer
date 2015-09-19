import os

from unittest import TestCase
from simulationAnalyzer import Reader as S

__author__ = 'smcho'

testName = "unittest"

class TestSimulationAnalyzer(TestCase):

    def setUp(self):
        self.p = S("unittest", "SimpleShareLogic", "b")

    def test_simulationAnalyzer(self):
        line = self.p.jsonMap


