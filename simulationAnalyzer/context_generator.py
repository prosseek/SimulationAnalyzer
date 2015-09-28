__author__ = 'smcho'

from simulationAnalyzer.host_base_generator import *
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

class ContextGenerator(HostBaseGenerator):

    def __init__(self, simulationName, strategy, id):
        super(ContextGenerator, self).__init__(simulationName, strategy, id)

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

