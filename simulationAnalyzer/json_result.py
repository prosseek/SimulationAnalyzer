__author__ = 'smcho'

import json
import os

from util.name import *

class JSONResult(object):
    def __init__(self, JSONFilePath):
        self.JSONFilePath = JSONFilePath
        self.result = self.loadJSON()
        self.trait = Name.resultFilePathToDict(JSONFilePath)

    def getHostToTuplesMap(self):
        return self.result['hostToTuplesMap']

    def getSummaries(self):
        return self.result['summaries']

    def loadJSON(self):
        def preconditionCheck():
            assert os.path.exists(self.JSONFilePath)
        def postConditionCheck():
            assert len(self.result > 0)

        preconditionCheck()

        with open(self.JSONFilePath) as data_file:
            return json.load(data_file)

        postConditionCheck()