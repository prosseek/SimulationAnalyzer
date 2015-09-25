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

def getFirstReceiveTime(a, groupId1, index1, groupId2, index2):
    showTime = a.showTime(groupId1, index1, groupId2, index2)
    if len(showTime): return showTime[0]

def getWhenBookLoverReceivesFromBookSeller1(a):
    return getFirstReceiveTime(a, "v", 1, "mb", 1)

def getWhenBookSeller1ReceivesFromBookLover(a):
    return getFirstReceiveTime(a, "mb", 1, "v", 1)

def getCoveragePercentageForBookLover(analyzer):
    return analyzer.getCoveragePercentage("v", 1)

def getResults(summaryType, simulationName):
    r = R(simulationName, "SimpleShareLogic", summaryType)
    c = C(r)
    a = A(c)

    #8115.7
    #3547.41
    #('g1c0', 4255.369759036144, 98.80952380952381, 83,        84)
    #  name   time               percent            covered    total

    bookLoverReceivesFromBookSeller1 =  getWhenBookLoverReceivesFromBookSeller1(a) # dissemination time
    bookSellerReceivesFromBookLover = getWhenBookSeller1ReceivesFromBookLover(a) # receive time
    coverageResults = getCoveragePercentageForBookLover(a) # spread rate / spread time
    return {"dt":bookLoverReceivesFromBookSeller1, "rt":bookSellerReceivesFromBookLover, "sr":coverageResults[2], "st":coverageResults[1]}

def getLaTeXString(simulationName):
    def normalize(input, inputReference):
        result = {}
        for key, value in input.items():
            ref = inputReference[key]
            if ref != 0.0:
                result[key] = 100.0*value/ref
            else:
                result[key] = -1.0
        return result

    resultJSON = getResults("j", simulationName)
    #print resultJSON
    resultLabeled = getResults("l", simulationName)
    resultFBF = getResults("b", simulationName)

    d = {}
    d["json"] = normalize(resultJSON, resultFBF)
    d["labeled"] = normalize(resultLabeled, resultFBF)
    d["fbf"] = normalize(resultFBF, resultFBF)

    template = """\
dissemination time &  {json[dt]}\%	 & {labeled[dt]}\%  & {fbf[dt]}\% \\\\
receive time       &  {json[rt]}\%	 & {labeled[rt]}\%	& {fbf[rt]}\% \\\\
spread rate        &  {json[sr]}\%   & {labeled[sr]}\%  & {fbf[sr]}\% \\\\
spread time        &  {json[st]}\%   & {labeled[st]}\%  & {fbf[st]}\% \\\\
""".format(**d)
    return template

if __name__ == "__main__":
    #simulationName = "unittest"
    simulationName = "open_air_book_fair"

    print "b:" + str(getResults("b", simulationName))
    print "l:" + str(getResults("l", simulationName))
    print "j:" + str(getResults("j", simulationName))

    print getLaTeXString(simulationName)

    # print a.showTime("v",1,"ma",1)[0]
    # print a.showTime("ma",1, "v", 1)[0]
    # print a.showTime("s",1, "v", 1)[0]
    #
    # # When market ma get the context from g1c0
    # print getFirstReceiveTime(a, "ma", 1, "v", 1)
    # print getFirstReceiveTime(a, "ma", 1, "mb", 1)
    # print getFirstReceiveTime(a, "v", 1, "ma", 1)
    # print getFirstReceiveTime(a, "v", 1, "mb", 1)
    # print getFirstReceiveTime(a, "v", 1, "mc", 1)
    # print getFirstReceiveTime(a, "v", 1, "md", 1)
    # print getFirstReceiveTime(a, "v", 1, "md", 1)
