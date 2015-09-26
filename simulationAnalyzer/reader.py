__author__ = 'smcho'

import json

from util.config import *


class Reader:
    def __init__(self, simulationName, strategy, id, baseDirectory = None):
        self.simulationName = simulationName
        self.strategy = strategy
        self.id = id
        self.path = Path(simulationName, strategy, id, baseDirectory)

        # 1. get the result file path, and load the JSON into map
        self.filePath = self.path.getResultsFilePath()
        self.jsonMap = self.loadJSON()

        # 2. get the configuration map (the c.txt file) and load it inot configMap
        self.configMapFilePath = self.config.getConfigurationFilePath(simulationName)
        self.configMap = self.config.readConfigurationFile(simulationName)
        self.groupIdAccList = self.createGroupIdAccList()
        self.groupToGroupIDMap = self.createGroupToGroupIDMap()

        # 3. get necessary information from the configuration map
        self.groupCount = self.configMap["Scenario.nrofHostGroups"]

    def loadJSON(self):
        with open(self.filePath) as data_file:
            return json.load(data_file)

    def createGroupIdAccList(self):
        """Returns a map of
           GroupId -> Acc
        """
        # 1. get the number of groups
        numberOfGroups =  self.configMap["Scenario.nrofHostGroups"]
        groupCount = []
        groupIDs = []
        for i in range(numberOfGroups):
            groupCount.append(self.configMap["Group{}.nrofHosts".format(i+1)] + (0 if i == 0 else groupCount[i-1]))
            groupIDs.append(self.configMap["Group{}.groupID".format(i+1)])
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        return zip(groupIDs, groupCount)

    def createGroupIdCountList(self):
        """Returns a map of
           GroupId -> Acc
        """
        # 1. get the number of groups
        numberOfGroups =  self.configMap["Scenario.nrofHostGroups"]
        groupCount = []
        groupIDs = []
        for i in range(numberOfGroups):
            groupCount.append(self.configMap["Group{}.nrofHosts".format(i+1)])
            groupIDs.append(self.configMap["Group{}.groupID".format(i+1)])
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        return zip(groupIDs, groupCount)

    def createGroupToGroupIDMap(self):
        result = {}
        for index, (groupID, acc) in enumerate(self.groupIdAccList):
            result[index+1] = groupID
        return result

    def getGroupCount(self): return int(self.groupCount)

    def getHostCount(self): return self.createGroupIdAccList()[-1][1]

