__author__ = 'smcho'

class Analyzer(object):
    def __init__(self, converter):
        self.converter = converter
        pass

    def getContexts(self, groupId, index):
        host = self.groupIdToHost(groupId, index)
        return self.jsonMap["hostToTuplesMap"][str(host)]

    def getTime(self, groupId1, index1, groupId2, index2):
        """
            groupId1/index1 finds the contexts of groupId2/index2

        :param groupId1:
        :param index1:
        :param groupId2:
        :param index2:
        :return:
        """
        contexts = self.getContexts(groupId1, index1)
        print contexts