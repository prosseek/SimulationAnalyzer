__author__ = 'smcho'

from simulationAnalyzer.context import *
from simulationAnalyzer.generator import *

class ContextGenerator(Generator):

    def __init__(self, simulationName, strategy, id, controlName):
        super(self.__class__, self).__init__(simulationName, strategy, id)
        self.jsonFilePaths = glob.glob(self.path.getContextPoolDirectory() + "*.json")
        self.path.getContextDirectory()

    def create(self):
        pass