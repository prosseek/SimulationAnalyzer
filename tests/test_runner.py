from unittest import TestCase
from simulationAnalyzer.config_generator import *
from simulationAnalyzer.context_generator import *
from simulationAnalyzer.util.path import *
from simulationAnalyzer.runner import *

__author__ = 'smcho'

class TestRunner(TestCase):

  def setUp(self):
      controlName = "control1.txt"
      self.cfg = ConfigGenerator("unittest", "SimpleShareLogic", "dynamic", controlName)
      self.cxg = ContextGenerator("unittest", "SimpleShareLogic", "dynamic")

      self.r = Runner(self.cfg.getPath())

  def test_create(self):
      self.cxg.create()
      results = self.cfg.create()
      self.assertTrue(len(results) > 0)

      configFilePath = results[0]
      # remove this with 'nosetests' test
      #self.r.run(configFilePath)

