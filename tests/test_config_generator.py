import os

from unittest import TestCase
from simulationAnalyzer.config_generator import *

__author__ = 'smcho'

class TestConfigGenerator(TestCase):

  def setUp(self):
      controlName = "control1.txt"
      self.g = ConfigGenerator("unittest", "SimpleShareLogic", "unittest", controlName)

  def test_create(self):
      results = self.g.create()
      #print results
      for r in results:
          self.assertTrue(os.path.exists(r))

