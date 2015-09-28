__author__ = 'smcho'

from simulationAnalyzer.generator import *
from simulationAnalyzer.util.group_parser import *
import glob

class ConfigBaseGenerator(Generator):

    def __init__(self, simulationName, strategy, id):
        super(ConfigBaseGenerator, self).__init__(simulationName, strategy, id)
        self.config = Config()




