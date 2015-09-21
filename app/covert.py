__author__ = 'smcho'

import argparse
import re

from simulationAnalyzer import Reader as R
from simulationAnalyzer import Converter as C

def listToContextName(l):
    try:
        groupName = l[0]
        index = int(l[1])
        i = c.groupIDIndexToHost(groupName, index)
        g = c.hostToGroup(i)

        print "g{}c{}".format(g, i)

    except Exception as e:
        print "ERROR => {}/{}".format(l, e)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Example with nonoptional arguments',
    )

    parser.add_argument('rest', nargs='*')
    parser.add_argument('-s', dest='simulationName', default="open_air_book_fair") # action="store",
    parser.add_argument('-l', dest='logic', default="SimpleShareLogic")
    parser.add_argument('-t', dest='summaryType', default="b")

    args = parser.parse_args()

    r = R(args.simulationName, args.logic, args.summaryType)
    c = C(r)

    if len(args.rest) == 2:
        listToContextName(args.rest)

    else:
        name = raw_input("groupId/index: ")
        while name:
            if name in ["q","Q"]:
                print "BYE"
                break
            names = re.compile("\s+").split(name)
            print names
            if len(names) == 2:
                listToContextName(names)
            name = raw_input("groupId/index:: ")
