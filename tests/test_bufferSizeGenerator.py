from unittest import TestCase
from simulationAnalyzer.buffer_size_generator import *

__author__ = 'smcho'

class TestBufferSizeGenerator(TestCase):
    def test_create(self):
        self.g = BufferSizeGenerator("unittest", "SimpleShareLogic", "dynamic")
