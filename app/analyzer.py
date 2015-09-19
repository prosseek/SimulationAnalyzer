__author__ = 'smcho'

from simulationAnalyzer import SimulationAnalyzer as S
from simulationAnalyzer import getResultFile

if __name__ == "__main__":
    simulationName = "open_air_book_fair"
    p = S(getResultFile(simulationName, "SimpleShareLogic", "b"))
    line = p.dict
    print line