import os

from unittest import TestCase
from simulationAnalyzer.util.property import *
from testUtils import *

__author__ = 'smcho'

class TestProperty(TestCase):
    def test_read(self):
        filePath = getTestResourceDirectory() + "hello.txt"
        p = Property()
        #print p.read(filePath)
        self.assertEqual(49, len(p.read(filePath)))

    def test_write(self):
        filePath = getTestResourceDirectory() + "__temp_hello.txt"
        dictionary = {"a":'10', "b":'20', "c":'30'}
        p = Property()
        p.write(filePath, dictionary)

        result = p.read(filePath)
        self.assertEqual(frozenset(dictionary.items()), frozenset(result.items()))
