import copy

from util.config import *
from util.path import *

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
        properties = p.read()
        print properties

    def create(self):
        destinationFilePath = Path.getConfigDirectory() + "/" + "???"
        groupsFilePath = Path.getGroupsFilePath()

        # We need to create a new control copy that contains all the information
        # including the simulationName/strategy to fill in the template and create the ONE simulatior configuration file.
        control = copy.deepcopy(self.control)
        control["simulationName"] = ""

        writeConfigurationFile(destinationFilePath, groupsFilePath, control)