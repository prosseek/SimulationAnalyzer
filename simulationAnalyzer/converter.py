__author__ = 'smcho'

import re

class Converter(object):

    def __init__(self, reader):
        self.reader = reader
        self.groupIdAccList = reader.groupIdAccList
        self.groupToGroupIDMap = reader.groupToGroupIDMap

    def hostToGroup(self, host):
        for i, (id, count) in enumerate(self.groupIdAccList):
            if host < count:
                return i+1

    def hostToGroupID(self, host):
        group = self.hostToGroup(host)
        groupID = self.groupToGroupIDMap[group]
        return groupID

    def hostToGroupIDIndex(self, host):
        """
        The idea is to get the previous value, and get the index from the difference

        # [('v', 1), ('s', 41), ('p', 81), ('ma', 82), ('mb', 83), ('mc', 84), ('md', 85)]
        self.assertTrue(('p', 16) == self.p.hostToGroupIDIndex(56)) # previous 41, 56 - 41 = 15, 15 + 1 == 16

        :param host:
        :return:
        """

        group = self.hostToGroup(host)
        groupID = self.groupToGroupIDMap[group]

        prev = 0
        for id, acc in self.groupIdAccList:
            if groupID == id:
                index = (host - prev + 1)
                break
            prev = acc
        return (groupID, index)

    def groupIDIndexToHost(self, groupId, count):
        count -= 1 # from the input 1 means the first, but from the index 1 is 0, so 1 should be reduced.
        prev = 0
        for id, acc in self.groupIdAccList:
            if groupId == id:
                result = prev + count
                if acc > result: return result
                else:
                    raise Exception("Out of range result: groupID({})/count({}) -> wrong (acc ({}) > result ({})) {}".format(groupId, count, acc, result, prev))
            prev = acc
        raise Exception("sum - {}".format(sum))

    def contextToGroupIDIndex(self, context):
        """
        self.assertEqual(("p", 29), self.p.contextToGroupIDIndex("g3c69l")) # 3rd group -> "p", prev 41, 69-41 = 28, 28+1 == 29

        :param context:
        :return:
        """
        def endswith(inputString, ends):
            for e in ends:
                if inputString.endswith(e): return True
            return False

        if endswith(context, ["l", "b", "j"]): context = context[:-1]
        r = re.compile("g(\d+)c(\d+)")
        g = r.search(context)
        if g:
            hostNumber = g.group(2)
            return self.hostToGroupIDIndex(int(hostNumber))

        raise Exception("Wrong format {}".format(context))

    def groupIDIndexToContext(self, groupID, index):
        host = self.groupIDIndexToHost(groupID, index)
        gMap = self.groupToGroupIDMap
        for key, value in gMap.items():
            if value == groupID:
                return "g{}c{}".format(key, host)

        raise Exception("Wrong values {}/{}".format(groupID, index))

