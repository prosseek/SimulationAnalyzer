import os
import glob

from unittest import TestCase
from simulationAnalyzer.util.path import *
from simulationAnalyzer.util.group_parser import *
from simulationAnalyzer.context_generator import *

__author__ = 'smcho'

class TestContextGenerator(TestCase):

    def setUp(self):
        self.p = Path("unittest", "SimpleShareLogic", "unittest")
        self.gp = GroupParser("unittest", "SimpleShareLogic", "unittest")

        contextDir = self.p.getContextDirectory()
        files = glob.glob(contextDir + "*.*")
        for f in files:
            os.unlink(f)
        self.g = ContextGenerator("unittest", "SimpleShareLogic", "unittest")


    def test_create(self):
        contextDir = self.p.getContextDirectory()
        files = glob.glob(contextDir + "*.*")
        self.assertTrue(len(files) == 0)
        self.g.create()
        files = glob.glob(contextDir + "*.*")

        expected = self.gp.getHostCount() * 2
        self.assertEqual(len(files), expected)
