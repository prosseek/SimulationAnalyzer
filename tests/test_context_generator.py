import os

from unittest import TestCase
from simulationAnalyzer.context_generator import *

__author__ = 'smcho'

class TestContextGenerator(TestCase):

    def setUp(self):
        self.g = ContextGenerator("unittest", "SimpleShareLogic", "unittest")

    def test_create(self):
        pass

