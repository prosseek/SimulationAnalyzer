import os

from unittest import TestCase
from simulationAnalyzer.util.property import *
from testUtils import *

__author__ = 'smcho'

class TestProperty(TestCase):
    def test_read(self):
        filePath = getTestResourceDirectory() + "hello.txt"
        p = Property(filePath)
        print p.read()
        self.assertEqual(49, len(p.read()))
