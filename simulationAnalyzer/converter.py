__author__ = 'smcho'

class Converter(object):

    def __init__(self, reader):
        self.reader = reader
        self.groupIdAccMap = reader.groupIdAccMap

    def hostToGroup(self, host):
        for i, (id, count) in enumerate(self.groupIdAccMap):
            #print i, count, id
            if host < count:
                #return "{}{}c{}".format(id, i+1, host)
                return i+1 # "g{}c{}".format(i+1, host)

    def groupIdToHost(self, groupId, count):
        count -= 1 # from the input 1 means the first, but from the index 1 is 0, so 1 should be reduced.
        prev = 0
        for id, acc in self.groupIdAccMap:
            if groupId == id:
                result = prev + count
                if acc > result: return result
                else:
                    raise Exception("Out of range result{} - range{}".format(result, prev+acc))
            prev = acc
        raise Exception("sum - {}".format(sum))

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