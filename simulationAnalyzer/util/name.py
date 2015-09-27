__author__ = 'smcho'

class Name(object):

    def __init__(self):
        pass

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