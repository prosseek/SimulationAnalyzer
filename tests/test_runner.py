from unittest import TestCase
from simulationAnalyzer.generator import *
from simulationAnalyzer.util.path import *
from simulationAnalyzer.runner import *

__author__ = 'smcho'

class TestRunner(TestCase):

  def setUp(self):
      self.p = Path("unittest", "SimpleShareLogic", "simple")
      controlName = "control1.txt"
      self.g = Generator(self.p, controlName)
      self.r = Runner(self.p)

  def test_create(self):
      results = self.g.create()
      self.assertTrue(len(results) > 0)

      configFilePath = results[0]
      # remove this with 'nosetests' test
      self.r.run(configFilePath)

