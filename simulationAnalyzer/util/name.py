__author__ = 'smcho'

import os

class Name(object):

    def __init__(self):
        pass

    @staticmethod
    def dictToResultFilePath(dict):
        def preconditionCheck(dict):
            assert "summaryType" in dict.keys()
            assert "maxIteration" in dict.keys()

        preconditionCheck(dict)
        summaryType = dict["summaryType"]
        del dict["summaryType"]
        maxIteration = dict["maxIteration"]
        del dict["maxIteration"]

        r = Name.dictToName(dict)
        return "{}-{}!{}.json".format(summaryType, maxIteration, r)



    @staticmethod
    def resultFilePathToDict(str):
        """
        Given a result file path
        .../b-1!endTime_5000!iteration_2!transmitRange_50.json

        :param str:
        :return:
        """

        # 1. extrat the file name from the file path

        resultFileName = str.split(os.sep)[-1]

        splitted = resultFileName.split("!")
        header = splitted[0]

        if "-" in header:
            # need more than 1 value to unpack
            # will be raised without
            (summaryType, iteration) = header.split("-")
        else:
            raise Exception("Format error %s" % header)

        rest = splitted[1:]
        dict = Name.nameToDict("!".join(rest).replace(".json",""))
        dict["summaryType"] = summaryType
        #dict["iteration"] = iteration
        return dict

    @staticmethod
    def dictToName(dict):
        """
        Given dictionary returns the name based on it

        :param dict:
        :return:
        """
        keys = sorted(dict.keys())

        result = ''
        for key in keys:
            result += '{}_{}!'.format(key, dict[key])
        return result[:-1]

    @staticmethod
    def nameToDict(str):
        result = {}
        splitted = str.split("!")
        for s in splitted:
            (key, value) = s.split("_")
            try:
                v = int(value)
            except ValueError:
                v = value
            result[key] = v

        return result