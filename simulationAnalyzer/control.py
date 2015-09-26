__author__ = 'smcho'

defaults = {
    "transmitRange":50,
    "endTime":10000,
    "iteration":1
}

class Control(object):

    def __init__(self, baseDirectory):
        self.baseDirectory = baseDirectory

