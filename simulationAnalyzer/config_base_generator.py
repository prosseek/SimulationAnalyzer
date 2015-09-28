__author__ = 'smcho'

from simulationAnalyzer.generator import *
from simulationAnalyzer.util.group_parser import *
import glob

class ConfigBaseGenerator(Generator):

    def __init__(self, simulationName, strategy, id):
        super(ConfigBaseGenerator, self).__init__(simulationName, strategy, id)

        self.samples = []
        self.marketContext = None
        jsonFilePaths = glob.glob(self.path.getContextPoolDirectory() + "*.json")
        # select only s1 .. s4
        for json in jsonFilePaths:
            if json.split(os.sep)[-1].startswith("s"):
                self.samples.append(json)
            else:
                self.marketContext = json

        self.contextDirectory = self.path.getContextDirectory()
        self.defautlBufferSizeFilePath = self.path.getDefaultBufferSizeFilePath()

        groupParser = GroupParser(simulationName, strategy, id)
        self.groupCount = groupParser.getHostCount()
        self.hostCount = groupParser.getHostCount()


