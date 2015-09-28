__author__ = 'smcho'

from simulationAnalyzer.util.config import *
from simulationAnalyzer.config_base_generator import *

class ConfigGenerator(ConfigBaseGenerator):

    def __init__(self, simulationName, strategy, id, controlName):
        super(self.__class__, self).__init__(simulationName, strategy, id)
        controlFilePath = self.path.getControlDirectory() + controlName
        self.control = self.config.read(controlFilePath)

    def create(self):
        if "summaryType" not in self.control:
            summaryType = "all"
        else:
            summaryType = self.control["summaryType"]

        if summaryType == "all":
            summaryType = ["b", "l", "j"]

        # We need to create a new control copy that contains all the information
        # including the simulationName/strategy to fill in the template and create the ONE simulatior configuration file.
        control = copy.deepcopy(self.control)
        if "summaryType" in self.control:
            del control["summaryType"]

        # The summaryType should not be in the filePath, so use control that removes it.
        groupsFilePath = self.path.getGroupsFilePath()
        iteration = int(control["iteration"])


        control["simulationName"] = self.path.getSimulationName()
        control["strategy"] = self.path.getStrategy()
        control["id"] = self.path.getId()
        # Where the context are found
        control["contextDirectory"] = self.path.getContextDirectory()

        result = []

        for i in range(iteration):
            c = {}
            c["iteration"] = (i + 1)
            c["transmitRange"] = control["transmitRange"]
            c["endTime"] = control["endTime"]
            nameFromDict = Name.dictToName(c)

            for s in summaryType:
                saveConfigFilePath = self.path.getConfigDirectory() + "/" + s + "-" + str(iteration) + "!" + nameFromDict + ".txt"
                resultFilePath = self.path.getResultDirectory() + "/" + s + "-" + str(iteration) + "!" + nameFromDict + ".json"

                control["summaryType"] = s
                control["resultFilePath"] = resultFilePath
                r = self.config.writeConfigurationFile(saveConfigFilePath, groupsFilePath, control)
                result.append(r)

        return result