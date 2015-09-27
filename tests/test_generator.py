from unittest import TestCase
from simulationAnalyzer.generator import *
from simulationAnalyzer.util.path import *

__author__ = 'smcho'

class TestGenerator(TestCase):

  def setUp(self):
      self.p = Path("unittest", "SimpleShareLogic", "simple")
      controlName = "control1.txt"
      self.g = Generator(self.p, controlName)

  def test_create(self):
      pass