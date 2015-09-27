# import os
#
# from unittest import TestCase
# from simulationAnalyzer import Reader as R
# from simulationAnalyzer.util.path import *
#
# __author__ = 'smcho'
#
# testName = "unittest"
#
# class TestReader(TestCase):
#     def setUp(self):
#         self.r = R("unittest", "SimpleShareLogic", "b")
#
#     def test_jsonMap(self):
#         j = self.r.jsonMap
#         self.assertEqual(len(j['hostToTuplesMap']), 84)
#         self.assertEqual(len(j['summaries']), 85)
#
