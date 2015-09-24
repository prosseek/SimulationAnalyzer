__author__ = 'smcho'

from simulationAnalyzer import Reader as R
from simulationAnalyzer import Converter as C
from simulationAnalyzer import Analyzer as A

from simulationAnalyzer import getResultFilePath

def percentage(analyzer, groupId, index):
    """
    The percentage of each node receives a host information
    :return:
    """
    analyzer.getCoveragePercentage(groupId, index)

    pass

def getFirstReceiveTime(analyzer, groupId1, index1, groupId2, index2):
    showTime = a.showTime("ma", 1, "v", 1)
    if showTime is None: return []
    else: return showTime

def getWhenBookLoverReceivesFromBookSeller1(analyzer):
    return getFirstReceiveTime(a, "ma", 1, "v", 1)

if __name__ == "__main__":
    simulationName = "unittest"
    r = R(simulationName, "SimpleShareLogic", "b")
    c = C(r)
    a = A(c)
    # When market ma get the context from g1c0
    print getFirstReceiveTime(a, "ma", 1, "v", 1)
    print getFirstReceiveTime(a, "ma", 1, "mb", 1)
    print getFirstReceiveTime(a, "v", 1, "ma", 1)
    print getFirstReceiveTime(a, "v", 1, "mb", 1)
    print getFirstReceiveTime(a, "v", 1, "mc", 1)
    print getFirstReceiveTime(a, "v", 1, "md", 1)
    print getFirstReceiveTime(a, "v", 1, "md", 1)