import copy
import os

from util.path import *
from util.group_parser import *
from util.name import *

__author__ = 'smcho'

class Generator(object):
    """
    Generator generates the configuration file to be stored
    """
    def __init__(self, simulationName, strategy, id):
        # path, controlFileName):
        self.path = Path(simulationName, strategy, id)
        self.groupParser = GroupParser(simulationName, strategy, id)

        self.contextDirectory = self.path.getContextDirectory()
        self.defaultBufferSizeFilePath = self.path.getDefaultBufferSizeFilePath()
        self.getDefaultBufferSizeFileName = self.defaultBufferSizeFilePath.split(os.sep)[-1]

        self.groupCount = self.groupParser.getHostCount()
        self.hostCount = self.groupParser.getHostCount()

    def getPath(self):
        return self.path
