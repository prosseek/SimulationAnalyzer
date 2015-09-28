__author__ = 'smcho'

from simulationAnalyzer.config_base_generator import *
from simulationAnalyzer.util.group_parser import *
import glob
import shutil
import random


class BufferSizeGenerator(ConfigBaseGenerator):

    def __init__(self, simulationName, strategy, id):
        super(BufferSizeGenerator, self).__init__(simulationName, strategy, id)
        self.defaultBufferSizeMap = self.config.readConfigurationFile(self.defaultBufferSizeFilePath)

    def create(self):
        dictionary = copy.deepcopy(self.defaultBufferSizeMap)
        for i in range(self.hostCount):
            groupNumber = self.groupParser.hostToGroup(i)
            groupIDIndex = self.groupParser.hostToGroupIDIndex(i)
            contextName = self.groupParser.groupIDIndexToContext(*groupIDIndex)

            if not contextName in dictionary:
                defaultValue = dictionary["default" + str(groupNumber)]
                dictionary[contextName] = defaultValue

        configFilePath = self.contextDirectory + self.getDefaultBufferSizeFileName
        with open(configFilePath, "w") as f:
            self.config.write(configFilePath, dictionary)