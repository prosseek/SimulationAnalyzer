__author__ = 'smcho'

import os

class Path(object):

    defaultBaseDirectory = "/Users/smcho/Desktop/code/ContextSharingSimulation/experiment/simulation/"
    baseDirectory = defaultBaseDirectory

    def __init__(self, simulationName, strategy, id, baseDirectory):
        if baseDirectory is not None:
            Path.baseDirectory = baseDirectory

        self.simulationName = simulationName
        self.strategy = strategy
        self.id = id

    @staticmethod
    def getBaseDirectory():
        return Path.baseDirectory

    @staticmethod
    def setBaseDirectory(bd):
        baseDirectory = bd

    def getResultsDirectory(self):
        return self.baseDirectory + "/output/results"

    def getResultsFilePath(self, controlDictionary):
        pass

    def getConfigurationFilePath(self, controlDictionary):
        simulationDirectory = Path.getBaseDirectory() + "/{}".format(self.simulationName)
        abspath = simulationDirectory + "/c.txt"
        return abspath

def getResultFilePath(simulationName, strategy, summaryType):
    simulationDirectory = Path.getBaseDirectory() + "/{}".format(simulationName)
    resultDirectory = simulationDirectory + "/results/"

    abspath = os.path.abspath("{resultDirectory}/result_smcho.{strategy}_{summaryType}.json".format(
        resultDirectory = resultDirectory, strategy = strategy, summaryType = summaryType))
    return abspath

def getConfigurationFilePath(simulationName):
    simulationDirectory = Path.getBaseDirectory() + "/{}".format(simulationName)
    abspath = simulationDirectory + "/c.txt"
    return abspath

