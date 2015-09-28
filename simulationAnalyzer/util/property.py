__author__ = 'smcho'

import ConfigParser

"""
Reads property file in verbatim (no interpretations) using ConfigParser
# http://stackoverflow.com/questions/2819696/parsing-properties-file-in-python/2819788#2819788

The ConfigParser requires

"""

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'

    def readline(self):
        if self.sechead:
            try:
                return self.sechead
            finally:
                self.sechead = None
        else:
            return self.fp.readline()

class Property(object):

    # def __init__(self, controlFilePath):
    #     self.controlFilePath = controlFilePath
    def read(self, controlFilePath):
        cp = ConfigParser.SafeConfigParser()
        cp.optionxform = str
        cp.readfp(FakeSecHead(open(controlFilePath)))
        return dict(cp.items('asection'))

    def write(self, controlFilePath, dictionary):
        keys = sorted(dictionary.keys())
        with open(controlFilePath, "w") as f:
            for key in keys:
                f.write("%s:%s\n" % (key, str(dictionary[key])))
