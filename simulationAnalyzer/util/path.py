__author__ = 'smcho'

import os

class Path(object):

    defaultBaseDirectory = "/Users/smcho/Desktop/code/ContextSharingSimulation/experiment/simulation/"
    baseDirectory = defaultBaseDirectory

    def __init__(self, simulationName, strategy, id, baseDirectory = None):
        if baseDirectory is not None:
            Path.baseDirectory = baseDirectory

        self.simulationName = simulationName
        self.strategy = strategy
        self.id = id
        self.preConditionCheck()

    def preConditionCheck(self):
        """
        This method checks if all the directories or files are existed
        :return:
        """
        for d in [
                  self.getGroupsFilePath(),
                  self.getControlDirectory(),
                  self.getContextDirectory(),
                  self.getConfigDirectory(),
                  self.getReportDirectory(),
                  self.getResultDirectory()]:
            assert os.path.exists(d), "Path does not exist %s" % d

    ############ baseDirectory
    @staticmethod
    def getBaseDirectory():
        return Path.baseDirectory

    @staticmethod
    def setBaseDirectory(bd):
        baseDirectory = bd

    ############ properties
    def getSimulationName(self):
        return self.simulationName

    def getStrategy(self):
        return self.strategy

    def getId(self):
        return self.id

    ############ id and input/output/control directory
    def getIdDirectory(self):
        return self.baseDirectory + "/%s/%s/%s/" % (self.simulationName, self.strategy, self.id)

    def getInputDirectory(self):
        return self.getIdDirectory() + "input/"

    def getOutputDirectory(self):
        return self.getIdDirectory() + "output/"

    def getControlDirectory(self):
        return self.getIdDirectory() + "control/"

    def getContextDirectory(self):
        return self.getInputDirectory() + "context/"

    def getResultDirectory(self):
        return self.getOutputDirectory() + "result/"

    def getReportDirectory(self):
        return self.getOutputDirectory() + "report/"

    def getConfigDirectory(self):
        return self.getOutputDirectory() + "config/"

    ############ id and input/output/control directory


    def getGroupsFilePath(self):
        return self.getInputDirectory() + "groups.txt"

    def getConfigurationFilePath(self, controlDictionary):
        simulationDirectory = Path.getBaseDirectory() + "/{}".format(self.simulationName)
        abspath = simulationDirectory + "/c.txt"
        return abspath

# def getResultFilePath(simulationName, strategy, summaryType):
#     simulationDirectory = Path.getBaseDirectory() + "/{}".format(simulationName)
#     resultDirectory = simulationDirectory + "/results/"
#
#     abspath = os.path.abspath("{resultDirectory}/result_smcho.{strategy}_{summaryType}.json".format(
#         resultDirectory = resultDirectory, strategy = strategy, summaryType = summaryType))
#     return abspath
#
# def getConfigurationFilePath(simulationName):
#     simulationDirectory = Path.getBaseDirectory() + "/{}".format(simulationName)
#     abspath = simulationDirectory + "/c.txt"
#     return abspath

