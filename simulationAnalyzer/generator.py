import copy

from util.config import *
from util.path import *
from util.name import *

__author__ = 'smcho'

class Generator(object):
    """
    Generator generates the configuration file to be stored
    """
    def __init__(self, path, controlFileName):
        self.path = path
        self.controlFileName = controlFileName
        self.controlFilePath = path.getControlDirectory() + "/" + controlFileName
        p = Property(self.controlFilePath)
        self.control = p.read()
        #print self.control

    def create(self):
        nameFromDict = Name.dictToName(self.control)
        groupsFilePath = self.path.getGroupsFilePath()
        iteration = int(self.control["iteration"])

        # We need to create a new control copy that contains all the information
        # including the simulationName/strategy to fill in the template and create the ONE simulatior configuration file.
        control = copy.deepcopy(self.control)
        control["simulationName"] = self.path.getSimulationName()
        control["strategy"] = self.path.getStrategy()
        control["id"] = self.path.getId()
        # Where the context are found
        control["directory"] = self.path.getContextDirectory()

        result = []

        for i in range(iteration + 1):
            for j in ["b","l","j"]:
                control["summaryType"] = j
                destinationFilePath = self.path.getConfigDirectory() + "/" + j + "-" + nameFromDict + ".txt"
                r = writeConfigurationFile(destinationFilePath, groupsFilePath, control)
                result.append(r)

        return result