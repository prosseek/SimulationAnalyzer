from simulationAnalyzer import Reader as R
from simulationAnalyzer import SingleAnalyzer as SA
from simulationAnalyzer import GroupParser as GP

from simulationAnalyzer.util.name import *
from simulationAnalyzer.util.path import *
from simulationAnalyzer.util.utility import *

__author__ = 'smcho'

def getFirstReceiveTime(a, groupId1, index1, groupId2, index2):
    showTime = a.showTime(groupId1, index1, groupId2, index2)
    if len(showTime): return showTime[0]

def getWhenBookLoverReceivesFromBookSeller1(a):
    return getFirstReceiveTime(a, "v", 1, "mb", 1)

def getWhenBookSeller1ReceivesFromBookLover(a):
    return getFirstReceiveTime(a, "mb", 1, "v", 1)

def getCoveragePercentageForBookLover(analyzer):
    return analyzer.getCoveragePercentage("v", 1)

def getResults(id, m):

    #print id,m

    simulationName = "open_air_book_fair"
    strategy = "SimpleShareLogic"

    r = R(simulationName, strategy, id)
    gp = GP(simulationName, strategy, id)

    results = r.get(m)
    #print results

    if len(results) > 0:
        result = results[0]
        a = SA(gp, result)

        #8115.7
        #3547.41
        #('g1c0', 4255.369759036144, 98.80952380952381, 83,        84)
        #  name   time               percent            covered    total

        bookLoverReceivesFromBookSeller1 =  getWhenBookLoverReceivesFromBookSeller1(a) # dissemination time
        bookSellerReceivesFromBookLover = getWhenBookSeller1ReceivesFromBookLover(a) # receive time
        coverageResults = getCoveragePercentageForBookLover(a) # spread rate / spread time
        return {"dt":bookLoverReceivesFromBookSeller1, "rt":bookSellerReceivesFromBookLover, "st":coverageResults[1]} # "sr":coverageResults[2],
    else:
        {}

if __name__ == "__main__":

    for summaryType in ['b','l','j']:
        times = [1000, 1500, 2000, 5000]
        for t in times:
            m = {
                'endTime': 15000,
                'iteration': 1,
                'maxIteration':5,
                'summaryType':summaryType,
                'transmitRange': 50
            }
            print getResults("simple_%d" % t, m)
        print "\n\n"


