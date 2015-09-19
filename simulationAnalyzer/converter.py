__author__ = 'smcho'

class Converter(object):

    def __init__(self, reader):
        self.reader = reader
        self.groupIdAccList = reader.groupIdAccList

    def hostToGroup(self, host):
        for i, (id, count) in enumerate(self.groupIdAccList):
            #print i, count, id
            if host < count:
                #return "{}{}c{}".format(id, i+1, host)
                return i+1 # "g{}c{}".format(i+1, host)

    def groupIdToHost(self, groupId, count):
        count -= 1 # from the input 1 means the first, but from the index 1 is 0, so 1 should be reduced.
        prev = 0
        for id, acc in self.groupIdAccList:
            if groupId == id:
                result = prev + count
                if acc > result: return result
                else:
                    raise Exception("Out of range result{} - range{}".format(result, prev+acc))
            prev = acc
        raise Exception("sum - {}".format(sum))

