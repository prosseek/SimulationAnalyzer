__author__ = 'smcho'

import json
from config import *
from pprint import pprint

class SimulationAnalyzer:
    def __init__(self, simulationName, strategy, summaryType):
        self.simulationName = simulationName
        self.strategy = strategy
        self.summaryType = summaryType

        self.filePath = getResultFile(simulationName, strategy, summaryType)
        self.dict = self.load()
        self.configMapFile = getConfigurationFile(simulationName)
        self.configMap = parseConfigurationFile(simulationName)
        self.groupCountIdMap = self.createGroupCountIdMap()

    def load(self):
        with open(self.filePath) as data_file:
            return json.load(data_file)

    def createGroupCountIdMap(self):
        """
        This is the context information that host 56 receives

        dict['56']

        [[0, 0, 0.0, u'g3c56b', 29],
         [19, 56, 4722.22, u'g2c40b', 29],
         [39, 56, 6849.11, u'g3c56b', 29],
         [65, 56, 5933.99, u'g2c27b', 29]],

         This method returns the group information of host 56 from
         1. u'g3c56b'
         2. configuration file
            Group3.groupID = p
            Group3.nrofHosts = 40

        From information 1, host 56 is group 3, and from information 2,
        Group3 has group id "P"

        So the mapping is
        p3c56 -> 56

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

    def hostToGroup(self, host):
        for i, (id, count) in enumerate(self.groupCountIdMap):
            #print i, count, id
            if host < count:
                #return "{}{}c{}".format(id, i+1, host)
                return i+1 # "g{}c{}".format(i+1, host)

    def groupIdToHost(self, groupId, count):
        count -= 1 # from the input 1 means the first, but from the index 1 is 0, so 1 should be reduced.
        prev = 0
        for id, acc in self.groupCountIdMap:
            if groupId == id:
                result = prev + count
                if acc > result: return result
                else:
                    raise Exception("Out of range result{} - range{}".format(result, prev+acc))
            prev = acc
        raise Exception("sum - {}".format(sum))

    def getContexts(self, groupId, index):
        host = self.groupIdToHost(groupId, index)
        return self.dict["hostToTuplesMap"][str(host)]