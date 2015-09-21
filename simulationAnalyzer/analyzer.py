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