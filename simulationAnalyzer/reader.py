__author__ = 'smcho'

from util.config import *

class Reader:
    def __init__(self, simulationName, strategy, id, baseDirectory = None):
        self.simulationName = simulationName
        self.strategy = strategy
        self.id = id
        self.path = Path(simulationName, strategy, id, baseDirectory)

        # 1. get the result file path, and load the JSON into map
        self.filePath = self.path.getResultsFilePath()
        self.jsonMap = self.loadJSON()






