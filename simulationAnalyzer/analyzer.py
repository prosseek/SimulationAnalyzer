__author__ = 'smcho'

import re

class Analyzer(object):
    def __init__(self, converter):
        self.converter = converter
        self.reader = converter.reader
        self.jsonMap = self.reader.jsonMap
        self.groupCount = self.reader.groupCount

    def toContextNames(self, contexts):
        """
        The contexts from JSON summary (using getContexts) is a list of a lot of contexts,
        they should be organized and be shown in a digestive way.

        Given contexts from JSON summary, this function returns the names of contexts
        in a readable way.

        This example shows the conversion from context name (g10c -> v1), and the context count.

        [('v1', 4)]
        [('p1', 3), ('p2', 3), ('p3', 3), ...
        ...
        [('md1', 3)]

        :param contexts:
        :return:
        """
        def grp(txt):
            r = re.search("\w(\d+)", txt)
            return int(r.group(1))

        result = {}
        for context in contexts:
            contextName = context[3]
            (gid, index) = self.converter.contextToGroupIDIndex(contextName)
            if gid not in result:
                result[gid] = []
            result[gid].append("{}{}".format(gid, index))

        res = []
        for c in range(1, self.groupCount + 1):
            groupId = self.converter.groupToGroupIDMap[c]
            res.append(sorted(result[groupId], key = lambda i: grp(i)))

        return res

    def getContexts(self, groupId, index):
        """
        From JSON result, we need to extract the contexts from groupId/index pair.
        For example, the first host in the "V" group (v/1) will be translated into context name
        such as g1c0 (first group, first host), as the JSON hosts stores information using the
        context name format.

        :param groupId:
        :param index:
        :return:
        """
        host = self.converter.groupIDIndexToHost(groupId, index)
        return self.jsonMap["hostToTuplesMap"][str(host)]

    def showTime(self, finderGroupId1, finderIndex1, groupId2, index2):
        """
            returns the time when
            groupId1/index1 finds the contexts of groupId2/index2

        :param finderGroupId1:
        :param finderIndex1:
        :param groupId2:
        :param index2:
        :return:
        """
        try:
            contexts = self.getContexts(finderGroupId1, finderIndex1)
            searchContextName = self.converter.groupIDIndexToContext(groupId2, index2)

            result = []
            for c in contexts:
                contextName = c[3]
                if contextName.startswith(searchContextName):
                    result.append(c[2])

            return sorted(result)
        except KeyError: # there is nothing in database
            return []

    def getAllMembers(self):
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        tupleList = self.reader.createGroupIdCountList()
        for (groupId, count) in tupleList:
            for i in range(count):
                id = i+1
                yield self.converter.groupIDIndexToContext(groupId, id)

    def getAllMembersGroupIDIndex(self):
        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        tupleList = self.reader.createGroupIdCountList()
        for (groupId, count) in tupleList:
            for i in range(count):
                id = i+1
                yield (groupId, id)


    def getCoveragePercentage(self, groupId, index):
        """
        groupId/index => contextName
        find the what percentage of the hosts receive the context contextName

        :param groupId:
        :param index:
        :return:
        """

        timeValues = []
        searchContextName = self.converter.groupIDIndexToContext(groupId, index)
        #print searchContextName
        for fidnerGroupId, finderIndex in self.getAllMembersGroupIDIndex():
            getTime = self.showTime(fidnerGroupId, finderIndex, groupId, index)
            #print fidnerGroupId, finderIndex, getTime[0] if len(getTime) else -1.0
            timeValues.append(getTime[0] if len(getTime) else -1.0)

        totalCount = self.reader.getHostCount() - 1 # exclude self
        coveredCount = len(filter(lambda x: x > 0, timeValues))
        averageTime = sum(filter(lambda x: x > 0, timeValues))/coveredCount
        #print totalCount, coveredCount
        return (searchContextName, averageTime, float(coveredCount)/float(totalCount)*100.0, coveredCount, totalCount)

