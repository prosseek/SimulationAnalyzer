from unittest import TestCase
from simulationAnalyzer.config_generator import *
from simulationAnalyzer.util.path import *
from simulationAnalyzer.runner import *

__author__ = 'smcho'

class TestRunner(TestCase):

  def setUp(self):
      controlName = "control1.txt"
      self.g = ConfigGenerator("unittest", "SimpleShareLogic", "unittest", controlName)
      self.r = Runner(self.g.getPath())

  def test_create(self):
      results = self.g.create()
      self.assertTrue(len(results) > 0)

      configFilePath = results[0]
      # remove this with 'nosetests' test
      #self.r.run(configFilePath)

