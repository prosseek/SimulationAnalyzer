__author__ = 'smcho'

from simulationAnalyzer.config_base_generator import *
from simulationAnalyzer.util.group_parser import *
import glob
import shutil
import random

config = """\
m = 0
k = 3
q = 16
complete = 0
"""

class ContextGenerator(Generator):

    def __init__(self, simulationName, strategy, id):
        super(ContextGenerator, self).__init__(simulationName, strategy, id)
        self.samples = []
        self.marketContext = None
        jsonFilePaths = glob.glob(self.path.getContextPoolDirectory() + "*.json")
        # select only s1 .. s4
        for json in jsonFilePaths:
            if json.split(os.sep)[-1].startswith("s"):
                self.samples.append(json)
            else:
                self.marketContext = json

    def create(self):
        for i in range(self.hostCount):
            groupIDIndex = self.groupParser.hostToGroupIDIndex(i)
            if groupIDIndex[0].startswith("s"):
                #print groupIDIndex
                sourceFilePath = self.marketContext

            else:
                sourceFilePath = random.sample(self.samples, 1)[0]

            contextName = self.groupParser.groupIDIndexToContext(*groupIDIndex)
            jsonContextFilePath = self.contextDirectory + contextName + ".json"
            shutil.copy(sourceFilePath, jsonContextFilePath)
            configFilePath = self.contextDirectory + contextName + ".conf"
            with open(configFilePath, "w") as f:
                f.write(config)

