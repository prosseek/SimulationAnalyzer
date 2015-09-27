__author__ = 'smcho'

from path import *
from config import *

class GroupParser(object):

    def __init__(self, simulationName, strategy, id, baseDirectory = None):

        def preconditionCheck():
            assert os.path.exists(self.groupsFilePath)
        self.p = Path(simulationName, strategy, id, baseDirectory)
        self.groupsFilePath = self.p.getGroupsFilePath()

        preconditionCheck()

        self.config = readConfigurationFile(self.groupsFilePath)

        # 1. get the configuration map (the c.txt file) and load it inot configMap
        self.groupIdAccList = self.createGroupIdAccList()
        self.groupToGroupIDMap = self.createGroupToGroupIDMap()

        # 2. get necessary information from the configuration map
        self.groupCount = self.config["Scenario.nrofHostGroups"]


    def createGroupIdAccList(self):
        """Returns a map of
           GroupId -> Acc
        """
        # 1. get the number of groups
        numberOfGroups =  self.config["Scenario.nrofHostGroups"]
        groupCount = []
        groupIDs = []
        for i in range(numberOfGroups):
            groupCount.append(self.config["Group{}.nrofHosts".format(i+1)] + (0 if i == 0 else groupCount[i-1]))
            groupIDs.append(self.config["Group{}.groupID".format(i+1)])
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        return zip(groupIDs, groupCount)

    def createGroupIdCountList(self):
        """Returns a map of
           GroupId -> Acc
        """
        # 1. get the number of groups
        numberOfGroups =  self.config["Scenario.nrofHostGroups"]
        groupCount = []
        groupIDs = []
        for i in range(numberOfGroups):
            groupCount.append(self.config["Group{}.nrofHosts".format(i+1)])
            groupIDs.append(self.config["Group{}.groupID".format(i+1)])
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        return zip(groupIDs, groupCount)

    def createGroupToGroupIDMap(self):
        result = {}
        for index, (groupID, acc) in enumerate(self.groupIdAccList):
            result[index+1] = groupID
        return result

    def getGroupCount(self): return int(self.groupCount)
    def getHostCount(self): return self.createGroupIdAccList()[-1][1]