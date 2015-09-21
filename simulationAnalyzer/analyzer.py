__author__ = 'smcho'

import re

class Analyzer(object):
    def __init__(self, converter):
        self.converter = converter
        self.reader = converter.reader
        self.jsonMap = self.reader.jsonMap
        self.groupCount = self.reader.groupCount
        pass

    def toContextNames(self, contexts):

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
        host = self.converter.groupIDIndexToHost(groupId, index)
        return self.jsonMap["hostToTuplesMap"][str(host)]

    def showTime(self, groupId1, index1, groupId2, index2):
        """
            returns the time when
            groupId1/index1 finds the contexts of groupId2/index2

        :param groupId1:
        :param index1:
        :param groupId2:
        :param index2:
        :return:
        """
        contexts = self.getContexts(groupId1, index1)
        print contexts