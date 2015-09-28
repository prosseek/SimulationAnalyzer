import copy

from util.config import *
from util.path import *
from util.name import *

__author__ = 'smcho'

class Generator(object):
    """
    Generator generates the configuration file to be stored
    """
    def __init__(self, simulationName, strategy, id):
        # path, controlFileName):
        self.path = Path(simulationName, strategy, id)

    def getPath(self):
        return self.path
