__author__ = 'smcho'

import glob

from util.groupsParser import *
from json_result import *

class Reader:
    def __init__(self, simulationName, strategy, id, baseDirectory = None):
        self.simulationName = simulationName
        self.strategy = strategy
        self.id = id

        self.path = Path(simulationName, strategy, id, baseDirectory)
        self.groupParser = GroupParser(simulationName, strategy, id, baseDirectory)

        self.jsonMap = self.readAllJSONFiles()

    def readAllJSONFiles(self):
        resultDirectory = self.path.getResultDirectory()
        jsonFilePaths = glob.glob(resultDirectory + "*.json")

        result = {}

        for json in jsonFilePaths:
            r = JSONResult(json)
            key = frozenset(r.trait.items())
            value = r
            result[key] = value

        return result





