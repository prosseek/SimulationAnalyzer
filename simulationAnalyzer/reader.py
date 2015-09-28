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

        self.jsonMap = self.__readAllJSONFiles()

    def __readAllJSONFiles(self):
        resultDirectory = self.path.getResultDirectory()
        jsonFilePaths = glob.glob(resultDirectory + "*.json")

        result = {}

        for json in jsonFilePaths:
            r = JSONResult(json)
            key = frozenset(r.trait.items())
            value = r
            result[key] = value

        return result

    def get(self, map):
        result = []
        allKeys = self.jsonMap.keys()

        # key can be smaller subset
        key = frozenset(map.items())
        for k in allKeys:
            if key.issubset(k):
                result.append(self.jsonMap[k])

        return result

    def getPath(self):
        return self.path



